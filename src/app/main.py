from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.user_repository_mock import UserRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.User import User


app = FastAPI()

repo = Environments.get_user_repo()

# @app.get("/items/get_all_items")
# def get_all_items():
#     items = repo.get_all_items()
#     return {
#         "items": [item.to_dict() for item in items]
#     }

@app.get("/")
def get_user_info():
    user_id = 1
    user = repo.get_item(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

        

# @app.post("/deposit", status_code=201)




handler = Mangum(app, lifespan="off")
