from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.User import User


class IUserRepository(ABC):
    
    
    @abstractmethod
    def get_all_items(self) -> List[User]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_item(self, User_id: int) -> Optional[User]:
        '''
        Returns the User with the given id.
        If the User does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_item(self, User: User, User_id: int) -> User:
        '''
        Creates a new User in the database
        '''
        pass
    
    @abstractmethod
    def delete_item(self, User_id: int) -> User:
        '''
        Deletes the User with the given id.
        If the User does not exist, returns None
        '''
        
    @abstractmethod
    def update_item(self, User_id:int, name:str=None, price:float=None, User_type:UserTypeEnum=None, admin_permission:bool=None) -> User:
        '''
        Updates the User with the given id.
        If the User does not exist, returns None
        '''
        pass
    
    