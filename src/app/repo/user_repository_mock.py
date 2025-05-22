from typing import Dict, Optional, List

from ..entities.User import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: Dict[int, User]
    
    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", account="0000", agency="00000-0", current_balance=1000.0),
            2: User(name="Barbie", account="0123", agency="01234-5", current_balance=1000.0),
            3: User(name="Lucas", account="0111", agency="01111-1", current_balance=1000.0),
            4: User(name="Pedro", account="0222", agency="22222-2", current_balance=1000.0)
        }
        
    def get_all_items(self) -> List[User]:
        return self.users.values()
    
    def get_item(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
    
    def create_item(self, user: User, user_id: int) -> User:
        self.users[user_id] = user
        return user
        
    
    def delete_item(self, user_id: int) -> User:
        user = self.users.pop(user_id, None)
        return user
        
        
    def update_item(self, user_id:int, name:str=None, account:str=None, agency:str=None, current_balance:float=None) -> User:
        user = self.users.get(user_id, None)
        if user is None:
            return None
        if name is not None:
            user.name = name
        if account is not None:
            user.account = account
        if agency is not None:
            user.agency = agency
        if current_balance is not None:
            user.current_balance = current_balance
        self.users[user_id] = user
        
        return user
        
    
    