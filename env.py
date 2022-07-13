from dotenv import load_dotenv
import os

load_dotenv()

DRIVER_PATH = os.environ.get('DRIVER_PATH')

MONGO_URL = os.environ.get('MONGO_URL')

DATABASE_NAME = os.environ.get('DATABASE_NAME')
COLLECTION_CAPSULE = os.environ.get('COLLECTION_CAPSULE')