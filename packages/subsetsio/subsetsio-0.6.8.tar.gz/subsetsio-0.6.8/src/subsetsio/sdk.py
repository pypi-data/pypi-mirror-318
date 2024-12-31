from typing import Dict, List, Optional, Any, Union, Tuple
from pathlib import Path
import requests
import json
import gzip
from dataclasses import dataclass

@dataclass
class ChartDiff:
    chart_id: str
    create: List[List[Any]]
    update: List[List[Any]]
    delete: List[List[Any]]

class ChartDiffer:
    @staticmethod
    def _extract_key(datapoint: List[Any]) -> Any:
        return datapoint[0]
        
    def diff_data(self, old_data: List[List[Any]], new_data: List[List[Any]]) -> ChartDiff:
        old_lookup = {self._extract_key(item): item for item in old_data}
        new_lookup = {self._extract_key(item): item for item in new_data}
        
        common_keys = set(old_lookup.keys()) & set(new_lookup.keys())
        removed_keys = set(old_lookup.keys()) - common_keys
        added_keys = set(new_lookup.keys()) - common_keys
        
        update_keys = {
            key for key in common_keys 
            if old_lookup[key] != new_lookup[key]
        }
        
        return ChartDiff(
            chart_id="",
            create=[new_lookup[k] for k in added_keys],
            update=[new_lookup[k] for k in update_keys],
            delete=[old_lookup[k] for k in removed_keys]
        )

class SubsetsClient:
    def __init__(self, api_key: str, api_url: str = "https://api.subsets.io", data_dir: str = "data"):
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')
        self.headers = {
            "X-API-Key": api_key,
            "Content-Encoding": "gzip",
            "Accept-Encoding": "gzip"
        }
        self.data_dir = Path(data_dir)
        self.charts_file = self.data_dir / "charts.jsonl"
        self.differ = ChartDiffer()

    def _load_charts(self) -> Dict[str, Dict[str, Any]]:
        charts = {}
        if self.charts_file.exists() and self.charts_file.stat().st_size > 0:
            with open(self.charts_file, 'r') as f:
                for line in f:
                    chart = json.loads(line)
                    charts[chart['sync_id']] = chart
        return charts

    def _save_charts(self, charts: Dict[str, Dict[str, Any]]) -> None:
        self.data_dir.mkdir(exist_ok=True)
        sorted_charts = dict(sorted(charts.items()))
        with open(self.charts_file, 'w') as f:
            for chart in sorted_charts.values():
                f.write(json.dumps(chart) + '\n')

    def _has_metadata_changes(self, old_chart: Dict[str, Any], new_chart: Dict[str, Any]) -> bool:
        metadata_fields = {'title', 'subtitle', 'description', 'icon', 'source_id', 'config', 'type'}
        return any(
            old_chart.get(field) != new_chart.get(field)
            for field in metadata_fields
        )

    def _gzip_json(self, data: Any) -> bytes:
        json_str = json.dumps(data)
        return gzip.compress(json_str.encode('utf-8'))

    def create(self, charts: List[Dict], batch_size=512) -> List[str]:
        all_chart_ids = []
        total_charts = len(charts)
        
        print(f"Starting batch creation of {total_charts} charts...")
        for i in range(0, total_charts, batch_size):
            batch = charts[i:i + batch_size]
            remaining = total_charts - (i + len(batch))
            print(f"Uploading batch of {len(batch)} charts... ({remaining} remaining)")
            
            gzipped_data = self._gzip_json(batch)
            response = requests.post(f"{self.api_url}/chart", headers=self.headers, data=gzipped_data)
            
            if response.status_code >= 400:
                print("Response headers:", response.headers)
                print("Response body:", response.text)
                response.raise_for_status()
                
            batch_chart_ids = response.json()["chart_ids"]
            print(f"Successfully created {len(batch_chart_ids)} charts in this batch")
            
            all_chart_ids.extend(batch_chart_ids)
            
        print(f"Batch creation complete. Total charts created: {len(all_chart_ids)}")
        return all_chart_ids

    def update_data(self, chart_data: Dict[str, Dict[str, List[List[Any]]]]) -> None:
        if chart_data:
            gzipped_data = self._gzip_json(chart_data)
            response = requests.put(f"{self.api_url}/chart/data", headers=self.headers, data=gzipped_data)
            response.raise_for_status()

    def update_metadata(self, chart_id: str, metadata: Dict[str, Any]) -> None:
        response = requests.put(f"{self.api_url}/chart/{chart_id}", headers=self.headers, json=metadata)
        response.raise_for_status()

    def delete(self, chart_ids: List[str]) -> None:
        if chart_ids:
            response = requests.delete(f"{self.api_url}/chart", headers=self.headers, json={"chart_ids": chart_ids})
            response.raise_for_status()

    def sync(self, charts_to_sync: List[Dict[str, Any]], remove_missing: bool = False, batch_size=512) -> None:
        existing_charts = self._load_charts()
        to_create = []
        data_updates = {}
        metadata_updates = {}

        current_sync_ids = {item["sync_id"] for item in charts_to_sync}
        
        for item in charts_to_sync:
            sync_id = item["sync_id"]
            chart = item["chart"]
            
            if sync_id in existing_charts:
                existing_chart = existing_charts[sync_id]["chart"]
                
                if self._has_metadata_changes(existing_chart, chart):
                    metadata_updates[sync_id] = {
                        k: v for k, v in chart.items() 
                        if k in {'title', 'subtitle', 'description', 'icon', 'source_id', 'config', 'type'} 
                        and v != existing_chart.get(k)
                    }
                
                old_data = existing_chart.get("data", [])
                new_data = chart.get("data", [])
                if old_data != new_data:
                    data_updates[sync_id] = (old_data, new_data)
            else:
                to_create.append(item)

        if remove_missing:
            to_delete = [
                existing_charts[sync_id]["chart_id"]
                for sync_id in existing_charts 
                if sync_id not in current_sync_ids
            ]
            if to_delete:
                print(f"Deleting {len(to_delete)} charts...")
                self.delete(to_delete)
                for sync_id in to_delete:
                    del existing_charts[sync_id]

        if to_create:
            print(f"Creating {len(to_create)} charts...")
            chart_datas = [item["chart"] for item in to_create]
            chart_ids = self.create(chart_datas, batch_size=batch_size)
            
            for item, chart_id in zip(to_create, chart_ids):
                sync_id = item["sync_id"]
                existing_charts[sync_id] = {
                    "sync_id": sync_id,
                    "chart": item["chart"],
                    "chart_id": chart_id
                }

        for sync_id, metadata in metadata_updates.items():
            print(f"Updating metadata for chart {sync_id}...")
            chart_id = existing_charts[sync_id]["chart_id"]
            self.update_metadata(chart_id, metadata)
            existing_charts[sync_id]["chart"].update(metadata)

        data_to_update = {}
        for sync_id, (old_data, new_data) in data_updates.items():
            diff = self.differ.diff_data(old_data, new_data)
            chart_id = existing_charts[sync_id]["chart_id"]
            
            operations = {}
            if diff.create:
                operations["create"] = diff.create
            if diff.update:
                operations["update"] = diff.update
            if diff.delete:
                operations["delete"] = diff.delete
                
            if operations:
                data_to_update[chart_id] = operations
                existing_charts[sync_id]["chart"]["data"] = new_data

        if data_to_update:
            print(f"Updating data for {len(data_to_update)} charts...")
            self.update_data(data_to_update)

        self._save_charts(existing_charts)