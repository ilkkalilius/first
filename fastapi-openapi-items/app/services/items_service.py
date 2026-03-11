from app.models.item import Item, ItemCreate


class ItemNotFoundError(Exception):
    """Raised when an item does not exist."""


class ItemsService:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id: int = 1

    def list_items(self) -> list[Item]:
        return list(self._items.values())

    def create_item(self, payload: ItemCreate) -> Item:
        item = Item(id=self._next_id, name=payload.name, description=payload.description)
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def get_item(self, item_id: int) -> Item:
        item = self._items.get(item_id)
        if item is None:
            raise ItemNotFoundError(f"Item {item_id} not found")
        return item

    def clear(self) -> None:
        self._items.clear()
        self._next_id = 1


items_service = ItemsService()
