import pytest
import time

from src.app.entities.transactions import Transactions
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionsRepositoryMock

class Test_TransactionsRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionsRepositoryMock()
        all_transactions = repo.get_all_transactions()
        assert len(all_transactions) == 3 
        assert all(isinstance(t, Transactions) for t in all_transactions)

    def test_get_transaction(self):
        repo = TransactionsRepositoryMock()
        transaction = repo.get_transaction(transaction_id="trans_1")
        assert transaction is not None
        assert transaction == repo.transactions.get("trans_1")

    def test_get_transaction_not_found(self):
        repo = TransactionsRepositoryMock()
        transaction = repo.get_transaction(transaction_id="trans_99")
        assert transaction is None
                
    def test_create_transaction(self):
        repo = TransactionsRepositoryMock()
        len_before = len(repo.transactions) 
        
        new_transaction_data = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            value=100.0,
            current_balance=2000.0,
            timestamp=time.time() * 1000
        )
        created_transaction = repo.create_transaction(transaction=new_transaction_data)
        len_after = len(repo.transactions)
        
        assert len_after == len_before + 1
        assert repo.transactions.get(f"trans_{len_after}") == new_transaction_data
        assert created_transaction == new_transaction_data

    def test_delete_transaction(self):
        repo = TransactionsRepositoryMock()
        transaction_id_to_delete = "trans_1"
        transaction_expected_to_be_deleted = repo.transactions.get(transaction_id_to_delete)
        len_before = len(repo.transactions)
        
        deleted_transaction = repo.delete_transaction(transaction_id=transaction_id_to_delete)
        len_after = len(repo.transactions)

        assert len_after == len_before - 1
        assert deleted_transaction == transaction_expected_to_be_deleted
        assert repo.transactions.get(transaction_id_to_delete) is None
        
    def test_delete_transaction_not_found(self):
        repo = TransactionsRepositoryMock()
        deleted_transaction = repo.delete_transaction(transaction_id="trans_99")
        assert deleted_transaction is None

    def test_update_transaction_full(self):
        repo = TransactionsRepositoryMock()
        transaction_id_to_update = "trans_1"
        
        new_type = TransactionTypeEnum.WITHDRAW
        new_value = 99.99
        new_balance = 1000.01
        new_timestamp = (time.time() + 60) * 1000

        updated_transaction = repo.update_transaction(
            transaction_id=transaction_id_to_update,
            transaction_type=new_type,
            value=new_value,
            current_balance=new_balance,
            timestamp=new_timestamp
        )
        
        fetched_transaction = repo.transactions.get(transaction_id_to_update)
        assert updated_transaction is not None
        assert fetched_transaction is not None
        assert updated_transaction == fetched_transaction
        
        assert fetched_transaction.transaction_type == new_type
        assert fetched_transaction.value == new_value
        assert fetched_transaction.current_balance == new_balance
        assert fetched_transaction.timestamp == new_timestamp
        
    def test_update_transaction_partial_type(self):
        repo = TransactionsRepositoryMock()
        transaction_id_to_update = "trans_2"
        original_transaction = repo.transactions.get(transaction_id_to_update)
        
        new_type = TransactionTypeEnum.DEPOSIT 
        if original_transaction.transaction_type == new_type:
            new_type = TransactionTypeEnum.WITHDRAW 

        updated_transaction = repo.update_transaction(transaction_id=transaction_id_to_update, transaction_type=new_type)
        
        assert updated_transaction.transaction_type == new_type
        assert repo.transactions.get(transaction_id_to_update).transaction_type == new_type
        assert updated_transaction.value == original_transaction.value
        assert updated_transaction.current_balance == original_transaction.current_balance

    def test_update_transaction_partial_value(self):
        repo = TransactionsRepositoryMock()
        transaction_id_to_update = "trans_3"
        original_transaction = repo.transactions.get(transaction_id_to_update)

        new_value = 123.45
        updated_transaction = repo.update_transaction(transaction_id=transaction_id_to_update, value=new_value)
        
        assert updated_transaction.value == new_value
        assert repo.transactions.get(transaction_id_to_update).value == new_value
        assert updated_transaction.transaction_type == original_transaction.transaction_type
        assert updated_transaction.current_balance == original_transaction.current_balance

    def test_update_transaction_not_found(self):
        repo = TransactionsRepositoryMock()
        updated_transaction = repo.update_transaction(transaction_id="trans_99", value=10.0)
        assert updated_transaction is None
