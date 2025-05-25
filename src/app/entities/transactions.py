from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum
import time
from datetime import datetime

class Transactions:
    transaction_type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: float
    
    def __init__(self, transaction_type: TransactionTypeEnum = None, value: float = None, current_balance: float = None, timestamp: float = None):
        
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type
        
        validation_value = self.validate_value(value)
        if validation_value[0] is False:
           raise ParamNotValidated("value", validation_value[1])        
        self.value = value
        
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
           raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance
        
        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
           raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp
        
    

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type == None:
            return [False, "transaction_type is Required "]
        if type(transaction_type) != TransactionTypeEnum:
            return [False, "transaction_type must be a TransactionTypeEnum type"]
        
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value == None:
            return [False, "value is Required "]
        if type(value) != TransactionTypeEnum:
            return [False, "value must be a float"]
        if value < 0:
            return[False, "value must be positive"]
        
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance == None:
            return [False, "current_balance is Required "]
        if type(current_balance) != TransactionTypeEnum:
            return [False, "current_balance must be a float"]
        if current_balance < 0:
            return[False, "current_balance must be positive"]
        
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
         # 1. Validação de obrigatoriedade
        if timestamp is None:
            return (False, "timestamp is Required")       
        if type(timestamp) is not float:
            return (False, "timestamp must be a float")
        if timestamp < 0:
            return (False, "timestamp must be a positive value")
        
        current_timestamp_ms = time.time() * 1000
        margin_ms = 5 * 60 * 1000 

        if timestamp > (current_timestamp_ms + margin_ms):
            return (False, "timestamp cannot be in the distant future")
        
        return (True, "")
        
    
        

