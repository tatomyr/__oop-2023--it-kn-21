from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PORT = os.getenv('PORT')
    DB_CONN_STRING = os.getenv('DB_CONN_STRING')
    DB_NAME = os.getenv('DB_NAME')
    SECRET = os.getenv('SECRET')


# Ви також можете додати додаткові конфігураційні параметри, які не залежать від .env файлу
