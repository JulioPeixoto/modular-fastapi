from dotenv import load_dotenv
import os

from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()
MONGO_URI = os.getenv("MONGODB_DBLOCAL_URI")


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri, maxPoolSize=50, minPoolSize=10)
        self.db = self.client[db_name]

    async def close(self):
        self.client.close()

    async def create_collections(self):
        try:
            collections = ["prompts"]
            for collection in collections:
                if collection not in await self.db.list_collection_names():
                    await self.db.create_collection(collection)
        except Exception as e:
            print(f"Erro ao criar collections no banco de dados: {e}")

mongodb = MongoDB(uri=MONGO_URI, db_name="transcricao_collection")
