from fastapi import FastAPI, status
from app.services.get_users import get_all_user
from app.services.create_user import create_new_user
from app.services.update_user import update_user_by_id
from app.services.delete_user import delete_user_by_id
from app.config.db_connection import SessionDep
from fastapi.responses import JSONResponse
from app.config.constants import DEBUG, PROJECT_NAME
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    debug=DEBUG, # False on production
    title=PROJECT_NAME,
    summary="This is a very simple crud application",
    description="This is very simple curd aplication",
    version="0.1.0",
    openapi_url="/simple_crud_openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=JSONResponse
)

@app.get("/get-users")
def get_users(session: SessionDep):
    data = get_all_user(session)
    responsedata = {
        "status_code":status.HTTP_200_OK,
        "message":"users list",
        "status":True,
        "data":data
    }
    encoded = jsonable_encoder(responsedata)
    response = JSONResponse(
        content=encoded,
        status_code=status.HTTP_200_OK
    )
    return response

@app.post("/create-user")
def create_user(session: SessionDep, userdata:dict):
    data = create_new_user(session,userdata)
    responsedata = {
        "status_code":status.HTTP_200_OK,
        "message": "New user created",
        "status":True,
        "data":data
    }
    encoded = jsonable_encoder(responsedata)
    response = JSONResponse(
        content=encoded,
        status_code=status.HTTP_200_OK
    )
    return response

@app.put("/update-user")
def update_user(session: SessionDep, userdata: dict):
    data = update_user_by_id(session, userdata)
    responsedata = {
        "status_code":status.HTTP_200_OK,
        "message": "New user updated",
        "status":True,
        "data":data
    }
    encoded = jsonable_encoder(responsedata)
    response = JSONResponse(
        content=encoded,
        status_code=status.HTTP_200_OK
    )
    return response


@app.delete("/delete-user")
def delete_user(session: SessionDep, userdata: dict):
    data = delete_user_by_id(session, userdata)
    responsedata = {
        "status_code":status.HTTP_200_OK,
        "message": "User deleted successfully",
        "status":True,
        "data": []
    }
    encoded = jsonable_encoder(responsedata)
    response = JSONResponse(
        content=encoded,
        status_code=status.HTTP_200_OK
    )
    return response