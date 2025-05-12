import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.repo.item_repository_mock import ItemRepositoryMock

class Test_ItemRepositoryMock:
    def test_get_all_items(self):
        repo = ItemRepositoryMock()
        assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
        
    def test_get_item(self):
        repo = ItemRepositoryMock()
        item = repo.get_item(item_id=1)
        assert item == repo.items.get(1)
    
    def test_get_item_not_found(self):
        repo = ItemRepositoryMock()
        item = repo.get_item(item_id=10)
        assert item is None
                
    def test_create_item(self):
        repo = ItemRepositoryMock()
        len_before = len(repo.items)
        item = Item(name="test", account="0000", agency="00000-0", current_balance=2000.0)
        repo.create_item(item=item, item_id=0)
        len_after = len(repo.items)
        assert len_after == len_before + 1
        assert repo.items.get(0) == item
        
    def test_delete_item(self):
        repo = ItemRepositoryMock()
        item_expected_to_be_deleted = repo.items.get(1)
        len_before = len(repo.items)
        
        item = repo.delete_item(item_id=1)
        len_after = len(repo.items)
        assert len_after == len_before - 1
        assert item == item_expected_to_be_deleted
        
    def test_delete_item_not_found(self):
        repo = ItemRepositoryMock()
        item = repo.delete_item(item_id=10)
        assert item is None

    def test_update_item(self):
        repo = ItemRepositoryMock()
        item = Item(name="test", account="0000", agency="00000-0", current_balance=2000.0)
        item_updated = repo.update_item(item_id=1, name=item.name, account=item.account, agency=item.agency, current_balance=item.current_balance)
        print(repo.items.get(1))
        assert item_updated == repo.items.get(1)
        
    def test_update_item_partial_1(self):
        repo = ItemRepositoryMock()
        name = "test"
        item_updated = repo.update_item(item_id=1, name=name)
        
        assert item_updated.name == name
        assert repo.items.get(1).name == name
        
    def test_update_item_partial_2(self):
        repo = ItemRepositoryMock()
        account = "0000"
        item_updated = repo.update_item(item_id=1, account=account)
        
        assert item_updated.account == account
        assert repo.items.get(1).account == account