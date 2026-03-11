from fastapi import APIRouter, HTTPException, status

from app.models.item import Item, ItemCreate
from app.services.items_service import ItemNotFoundError, items_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[Item], summary="List items")
def list_items() -> list[Item]:
    return items_service.list_items()


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED, summary="Create item")
def create_item(payload: ItemCreate) -> Item:
    return items_service.create_item(payload)


@router.get("/{item_id}", response_model=Item, summary="Get item by id")
def get_item(item_id: int) -> Item:
    try:
        return items_service.get_item(item_id)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
