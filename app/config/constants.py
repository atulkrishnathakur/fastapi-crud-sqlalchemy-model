from decouple import config

PROJECT_NAME = config("PROJECT_NAME", default='', cast=str)
DEBUG = config("DEBUG", default=False, cast=bool)
DB_DRIVER = config("DB_DRIVER", default='mysql+pymysql', cast=str)
DB_HOST = config("DB_HOST", default='localhost', cast=str)
DB_NAME = config("DB_NAME", default='fastapi_crud_1', cast=str)
DB_USER = config("DB_USER", default='root', cast=str)
DB_PASSWORD = config("DB_PASSWORD", default='123456789', cast=str)

DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"