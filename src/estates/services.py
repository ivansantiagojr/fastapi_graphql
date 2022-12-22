from dataclasses import asdict

from src.database import database
from src.estates.models import Estate, EstateIn


async def create_estate_db(estate: EstateIn):
    new_estate = asdict(estate)
    result = await database["estates"].insert_one(new_estate)

    if result is not None or result.inserted_id is not None:
        return Estate(**new_estate)

    return None


async def find_all_db():
    cursor = database["estates"].find()

    return [Estate(**document) for document in await cursor.to_list(length=100)]
