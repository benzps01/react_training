from dotenv import load_dotenv
import os
load_dotenv()

class ApplicationConfig:
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    id = os.environ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}' 