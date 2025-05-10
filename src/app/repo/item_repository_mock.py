from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.item import Item
from .item_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    items: Dict[int, Item]
    
    def __init__(self):
        self.items = {
            1: Item(name="Barbie", account="0123", agency="01234-5", current_balance=1000.0),
            2: Item(name="Lucas", account="0111", agency="01111-1", current_balance=1000.0),
            3: Item(name="Vitor", account="0000", agency="00000-0", current_balance=1000.0),
            4: Item(name="Pedro", account="0222", agency="22222-2", current_balance=1000.0)
        }
        
    def get_all_items(self) -> List[Item]:
        return self.items.values()
    
    def get_item(self, item_id: int) -> Optional[Item]:
        return self.items.get(item_id, None)
    
    def create_item(self, item: Item, item_id: int) -> Item:
        
        self.items[item_id] = item
        return item
    
    def delete_item(self, item_id: int) -> Item:
        item = self.items.pop(item_id, None)
        return item
        
        
    def update_item(self, item_id:int, name:str=None, account:str=None, agency:str=None, current_balance:float=None) -> Item:
        item = self.items.get(item_id, None)
        if item is None:
            return None
        
        if name is not None:
            item.name = name
        if account is not None:
            item.account = account
        if agency is not None:
            item.agency = agency
        if current_balance is not None:
            item.current_balance = current_balance
        self.items[item_id] = item
        
        return item
        
    
    