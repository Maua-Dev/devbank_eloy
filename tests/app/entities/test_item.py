import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_Item:
    def test_item(self):
        item = Item("test", "0123", "01234-5", 2000.0)
        assert item.name == "test"
        assert item.account == "0123"
        assert item.agency == "01234-5"
        assert item.current_balance == 2000.0
        
    def test_item_dict(self):
        item = Item("test", "0123", "01234-5", 2000.0)
        assert item.to_dict() == {'name': 'test', 'account': '0123', 'agency': '01234-5', 'current balance': 2000.0}
    
    def test_item_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            Item(account = '0123', agency = '01234-5', current_balance=2000.0)
   
    def test_item_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Item(name = 20, account='0123',agency = '01234-5', current_balance = 2000.0)
    
    def test_item_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Item(name="Vi", account = "0123", agency = "01234-5", current_balance = 2000.0) 
    
    def test_item_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", agency = "01234-5", current_balance = 2000.0 )      
    
    def test_item_account_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = 250 ,agency = "01234-5", current_balance = 2000.0 )   
    
    def test_item_account_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "012" ,agency = "01234-5", current_balance = 2000.0 )     
    
    def test_item_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" , current_balance = 2000.0 )
    
    def test_item_agency_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" ,agency = 12345, current_balance = 2000.0 )
    
    def test_item_agency_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" ,agency = "0123", current_balance = 2000.0 )

    def test_item_currentbalance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" ,agency = "0123")
    
    def test_item_currentbalance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" ,agency = "0123", current_balance = -1 )
    
    def test_item_currentbalance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Item(name = "Test", account = "0123" ,agency = "0123", current_balance = "2000.0" )
           
    
    