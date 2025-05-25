from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.user_repository_mock import UserRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.transaction_type_enum import ItemTypeEnum

from .entities.User import User


app = FastAPI()

user_repo = Environments.get_user_repo()
#transaction_repo = Enviroments.get_transactions_repo()


@app.get("/")
def get_user_info():
    user_id = 1
    user = user_repo.get_item(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

        

# @app.post("/deposit", status_code=201)




handler = Mangum(app, lifespan="off")
