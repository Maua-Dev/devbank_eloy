import pytest
import time
from enum import Enum

from src.app.entities.transactions import Transactions
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class Test_Transactions:

    def test_transaction_creation(self):
        transaction = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            value=150.75,
            current_balance=2150.75,
            timestamp=time.time() * 1000
        )
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert transaction.value == 150.75
        assert transaction.current_balance == 2150.75
        assert isinstance(transaction.timestamp, float)

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(value=100.0, current_balance=200.0, timestamp=time.time() * 1000)

    def test_transaction_type_is_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type="DEPOSIT", value=100.0, current_balance=200.0, timestamp=time.time() * 1000)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, current_balance=200.0, timestamp=time.time() * 1000)

    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value="100.0", current_balance=200.0, timestamp=time.time() * 1000)

    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=-50.0, current_balance=200.0, timestamp=time.time() * 1000)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, timestamp=time.time() * 1000)

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance="200.0", timestamp=time.time() * 1000)
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=-1.0, timestamp=time.time() * 1000)

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=200.0)

    def test_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=200.0, timestamp=123456789)

    def test_timestamp_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=200.0, timestamp=-12345.678)

    def test_timestamp_is_in_future(self):
        future_timestamp = (time.time() + 10 * 60) * 1000
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance=200.0,
                timestamp=future_timestamp
            )