from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.User import User


class IUserRepository(ABC):
    
    @abstractmethod
    def get_item(self) -> Optional[User]:
        '''
        Returns the User with the given id.
        If the User does not exist, returns None
        '''
        pass
    
    