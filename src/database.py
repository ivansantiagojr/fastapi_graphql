from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import settings

db_url = settings.DB_URL
mongo_client = AsyncIOMotorClient(db_url)

db_name = settings.DB_NAME
database = mongo_client.db_name


def get_db() -> AsyncIOMotorDatabase:
    return AsyncIOMotorClient(db_url)[db_name]


async def get_collection(collection_name: str):
    return await get_db()[collection_name]


async def get_record(collection: str, query: dict) -> dict:
    return await get_db()[collection].find_one(query, {"id": False})
