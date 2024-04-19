from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMINS = os.getenv('ADMINS')

DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')