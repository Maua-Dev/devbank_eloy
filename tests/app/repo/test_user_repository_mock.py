import pytest
from src.app.entities.User import User
from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_UserRepositoryMock:
    def test_get_all_items(self):
        repo = UserRepositoryMock()
        assert all([user_expect == user for user_expect, user in zip(repo.users.values(), repo.get_all_items())]) 
        
    def test_get_item(self):
        repo = UserRepositoryMock()
        user = repo.get_item(user_id=1)
        assert user == repo.users.get(1)
    
    def test_get_item_not_found(self):
        repo = UserRepositoryMock()
        user = repo.get_item(user_id=10)
        assert user is None
                
    def test_create_item(self):
        repo = UserRepositoryMock()
        len_before = len(repo.users)
        user = User(name="test", account="0000", agency="00000-0", current_balance=2000.0)
        repo.create_item(user=user, user_id=0)
        len_after = len(repo.users)
        assert len_after == len_before + 1
        assert repo.users.get(0) == user
        
    def test_delete_item(self):
        repo = UserRepositoryMock()
        user_expected_to_be_deleted = repo.users.get(1)
        len_before = len(repo.users)
        
        user = repo.delete_item(user_id=1)
        len_after = len(repo.users)
        assert len_after == len_before - 1
        assert user == user_expected_to_be_deleted
        
    def test_delete_item_not_found(self):
        repo = UserRepositoryMock()
        user = repo.delete_item(user_id=10)
        assert user is None

    def test_update_item(self):
        repo = UserRepositoryMock()
        user = User(name="test", account="0000", agency="00000-0", current_balance=2000.0)
        user_updated = repo.update_item(user_id=1, name=user.name, account=user.account, agency=user.agency, current_balance=user.current_balance)
        print(repo.users.get(1))
        assert user_updated == repo.users.get(1)
        
    def test_update_item_partial_1(self):
        repo = UserRepositoryMock()
        name = "test"
        user_updated = repo.update_item(user_id=1, name=name)
        
        assert user_updated.name == name
        assert repo.users.get(1).name == name
        
    def test_update_item_partial_2(self):
        repo = UserRepositoryMock()
        account = "0000"
        user_updated = repo.update_item(user_id=1, account=account)
        
        assert user_updated.account == account
        assert repo.users.get(1).account == account