from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL")
__ORIGINS__ = os.getenv("ORIGINS")
DEBUG = os.getenv("DEBUG")
ENVIRONMENT = os.getenv("ENVIRONMENT")