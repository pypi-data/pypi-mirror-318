import pandas as pd
import os
import json
import gzip
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any
from collections import defaultdict
from pydantic import ValidationError as PydanticValidationError
from subsetsio.models.chart import parse_chart
import requests

@dataclass
class ValidationErrorSummary:
    error_type: str
    message: str
    examples: List[Dict[str, Any]]
    total_occurrences: int
    charts_affected: List[str]

class ValidationError(Exception):
    def __init__(self, error_summaries: List[ValidationErrorSummary], max_examples: int = 3):
        self.error_summaries = error_summaries
        self.max_examples = max_examples
        
        error_details = []
        for summary in error_summaries:
            examples = summary.examples[:max_examples]
            omitted = len(summary.examples) - max_examples if len(summary.examples) > max_examples else 0
            
            error_details.extend([
                f"\nError Type: {summary.error_type}",
                f"Message: {summary.message}",
                f"Affected Charts: {len(summary.charts_affected)}",
                f"Total Occurrences: {summary.total_occurrences}",
                "Examples:"
            ])
            
            error_details.extend(f"  - {example}" for example in examples)
            if omitted > 0:
                error_details.append(f"  ... {omitted} more similar errors omitted")
        
        super().__init__("Validation failed:\n" + "\n".join(error_details))

class SubsetsClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = os.getenv("SUBSETS_API_URL", "https://api.subsets.io")
        self.headers = {
            "X-API-Key": api_key,
            "Content-Encoding": "gzip",
            "Accept-Encoding": "gzip"
        }
        self.data_dir = Path(os.getenv('DATA_DIR', 'data'))
        self.state_file = self.data_dir / 'sync_state.csv'

    def _group_validation_errors(self, errors: List[Dict[str, Any]], max_examples: int = 3) -> List[ValidationErrorSummary]:
        error_groups = defaultdict(list)
        
        for chart_idx, error in enumerate(errors):
            if "error" in error:
                if isinstance(error["error"], list):  # Pydantic validation errors
                    for e in error["error"]:
                        key = (e.get("type", "unknown"), str(e.get("msg", "")))
                        error_groups[key].append({
                            "chart_index": chart_idx,
                            "location": e.get("loc", []),
                            "detail": e
                        })
                else:  # Other exceptions
                    key = (error["error"].__class__.__name__, str(error["error"]))
                    error_groups[key].append({
                        "chart_index": chart_idx,
                        "detail": error["error"]
                    })

        return [
            ValidationErrorSummary(
                error_type=error_type,
                message=message,
                examples=group[:max_examples],
                total_occurrences=len(group),
                charts_affected=sorted(set(str(e["chart_index"]) for e in group))
            )
            for (error_type, message), group in sorted(
                error_groups.items(), 
                key=lambda x: len(x[1]), 
                reverse=True
            )
        ]

    def validate(self, charts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate charts without making API calls."""
        errors = []
        for i, chart in enumerate(charts):
            try:
                parse_chart(chart)
            except PydanticValidationError as e:
                errors.append({"chart_index": i, "error": e.errors()})
            except Exception as e:
                errors.append({"chart_index": i, "error": e})
        
        if errors:
            raise ValidationError(self._group_validation_errors(errors))
        return []

    def _gzip_json(self, data: Any) -> bytes:
        return gzip.compress(json.dumps(data).encode('utf-8'))

    def _load_state(self) -> Dict[str, str]:
        return pd.read_csv(self.state_file).set_index('source_id')['last_update'].to_dict() if self.state_file.exists() else {}

    def _save_state(self, state: Dict[str, str]):
        self.data_dir.mkdir(exist_ok=True)
        pd.DataFrame([{'source_id': k, 'last_update': v} for k, v in state.items()]).to_csv(self.state_file, index=False)

    def sync(self, charts: List[Dict]) -> None:
        # Validate all charts first
        self.validate(charts)
        
        state = self._load_state()
        by_source = {chart['tags']['id']: chart for chart in charts}
        
        to_create = []
        to_update = {}
        
        for source_id, chart in by_source.items():
            if not (data := chart.get('data')):
                continue
                
            last_date = data[-1][0]  # Assuming timestamp is first element
            if source_id not in state:
                to_create.append(chart)
            elif last_date > state[source_id]:
                to_update[source_id] = [p for p in data if p[0] > state[source_id]]
            state[source_id] = last_date
            
        if to_create:
            requests.post(f"{self.api_url}/chart", headers=self.headers, data=self._gzip_json(to_create)).raise_for_status()
            
        if to_update:
            requests.post(f"{self.api_url}/chart/data/rows", headers=self.headers, data=self._gzip_json(to_update)).raise_for_status()
            
        self._save_state(state)