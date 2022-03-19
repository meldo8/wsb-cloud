from decouple import config

SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL", cast=str)
API_KEY = config("API_KEY", cast=str)
