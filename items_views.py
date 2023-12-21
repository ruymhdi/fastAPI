from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def list_items():
	return [
		"items1",
		"items2",
	]


@router.get("/items/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
	return {
		"item": {
			"id": item_id,
		},
	}

@router.get("/items/latest/")
def get_lates_item():
	return {"item": {"id": "0", "name": "latest"}}
