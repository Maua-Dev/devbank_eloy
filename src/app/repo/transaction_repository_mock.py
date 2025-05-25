from typing import Dict, Optional, List
import time

from ..entities.transactions import Transactions
from ..enums.transaction_type_enum import TransactionTypeEnum
from .transaction_repository_interface import ITransactionsRepository

class TransactionsRepositoryMock(ITransactionsRepository):
    transactions: Dict[str, Transactions]
    _next_id_counter: int

    def __init__(self):
        self._next_id_counter = 0
        self.transactions = {}
        
        ts1 = time.time() * 1000
        transaction1 = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            value=250.50,
            current_balance=1250.50,
            timestamp=ts1
        )
        self.create_transaction(transaction1) 

        time.sleep(0.01) 
        ts2 = time.time() * 1000
        transaction2 = Transactions(
            transaction_type=TransactionTypeEnum.WITHDRAW,
            value=75.00,
            current_balance=1175.50,
            timestamp=ts2
        )
        self.create_transaction(transaction2)

        time.sleep(0.01)
        ts3 = time.time() * 1000
        transaction3 = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            value=500.00,
            current_balance=1675.50,
            timestamp=ts3
        )
        self.create_transaction(transaction3)

    def _generate_id(self) -> str:
        self._next_id_counter += 1
        return f"trans_{self._next_id_counter}"

    def get_transaction(self, transaction_id: str) -> Optional[Transactions]:
        return self.transactions.get(transaction_id)

    def get_all_transactions(self) -> List[Transactions]:
        return list(self.transactions.values())

    def create_transaction(self, transaction: Transactions) -> Transactions:
        transaction_id = self._generate_id()
        self.transactions[transaction_id] = transaction
        return transaction 

    def delete_transaction(self, transaction_id: str) -> Optional[Transactions]:
        return self.transactions.pop(transaction_id, None)
        
    def update_transaction(self, 
                           transaction_id: str, 
                           transaction_type: Optional[TransactionTypeEnum] = None, 
                           value: Optional[float] = None, 
                           current_balance: Optional[float] = None, 
                           timestamp: Optional[float] = None) -> Optional[Transactions]:
        transaction = self.transactions.get(transaction_id)
        if transaction is None:
            return None

        if transaction_type is not None:
            transaction.transaction_type = transaction_type
        
        if value is not None:
            transaction.value = value
            
        if current_balance is not None:
            transaction.current_balance = current_balance
            
        if timestamp is not None:
            transaction.timestamp = timestamp
        
        self.transactions[transaction_id] = transaction
        return transaction
