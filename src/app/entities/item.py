from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class Item:
    name: str
    account: str
    agency: str
    current_balance: float
    
    def __init__(self, name: str=None,  account : str=None, agency: str=None, current_balance: float = None):
        
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_name[1])
        self.account = account
        
        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency
        
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current balance", validation_agency[1])
        self.current_balance = current_balance
        
        
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")

    @staticmethod
    def validate_account(account: float) -> Tuple[bool, str]:
        if account is None:
            return(False, "Account is required")
        if type(account) != str:
            return(False, "Account must be a string")
        if len(account) != 4:
            return(False, "Account must have 4 numbers")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency: str) -> Tuple [bool, str]:
        if agency is None:
            return(False, "Agency is required")
        if type(agency)!= str:
            return(False, "Agency must be a string")
        if len(agency)!= 6:
            return (False, "Agency must have 6 characters")
        return (True, "")
    
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return(False, "Current Balance is required")
        if type(current_balance) != float:
            return(False, "Current Balance must be a float")
        if current_balance < 0:
            return(False, "Current Balance must be 0 or a positive number")
        return (True, "")
    
    def to_dict(self):
       return {
           "name": self.name,
           "account": self.account,
           "agency": self.agency,
           "current_balance": self.current_balance
       }
    
    