from typing import Any, Dict, Optional

from pydantic import BaseModel


class Document(BaseModel):
    id: int
    uid: str
    display_name: str
    value: Dict[str, Any]
    file_hash: Optional[str]
    gcs_path: str
    user_id: Optional[int] = None
    status: str
    created_at: str
    updated_at: str


class Batch(BaseModel):
    id: int
    uid: str
    name: str
    status: str
    project_id: int
    created_at: str
    updated_at: str


class BatchWithDocuments(Batch):
    documents: list[Document]


class GetBatchesResponse(BaseModel):
    batches: list[BatchWithDocuments]


class Batches:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    def list(self):
        response = self.client.get(f"{self.base_url}/public/v1/batches")
        response.raise_for_status()
        return GetBatchesResponse(**response.json())

    def get_status(self, batch_uid: str):
        response = self.client.get(f"{self.base_url}/public/v1/batches/{batch_uid}")
        response.raise_for_status()

        response_json = response.json() or {}
        return response_json.get("batch", {}).get("status")


class BatchesAsync:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    async def list(self):
        response = await self.client.get(f"{self.base_url}/public/v1/batches")
        response.raise_for_status()
        return GetBatchesResponse(**response.json())

    async def get_status(self, batch_uid: str):
        response = await self.client.get(
            f"{self.base_url}/public/v1/batches/{batch_uid}"
        )
        response.raise_for_status()

        response_json = response.json() or {}
        return response_json.get("batch", {}).get("status")
