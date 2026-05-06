# About this project
1. This is a very simple crud project with FastAPI framework
2. MySQL used for database
3. SQLAlchemy orm model used to execute mysql queries
4. python-decouple(https://pypi.org/project/python-decouple/) library used to get data from env file


# jsonable_encoder
1. jsonable_encoder is better than json.dict() 
2. jsonable_encoder converts python objects to json ready dict/list
3. jsonable_encoder makes datetime, UUID, Enum, Pydantic models, sets, frozensets to JSON‑friendly


# password hashing
1. Reference: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords 
1. install the `pip install "pwdlib[argon2]"` for password hashing
```
(venv) atulkrishnathakur@atul-pc:~/fastapi_projects/fastapi-crud-sqlalchemy-model$ pip install "pwdlib[argon2]"
```
