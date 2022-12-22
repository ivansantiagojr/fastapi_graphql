from src.estates.services import create_estate_db, find_all_db

from .models import Estate, EstateIn


# mutation create estate
async def create_estate(estate: EstateIn) -> Estate:
    return await create_estate_db(estate)


# query find all estates
async def find_estates() -> list[Estate]:
    return await find_all_db()


# estate_test = EstateIn(
#    title="asdf",
#    realtor="asdf",
#    description="asdf",
#    price=123,
#    address="asdf",
#    parking_spaces=3,
#    furnished=True,
#    other_costs=None,
#    created_on=None,
#    last_updated_on=None,
# )

# print(asdict(estate_test))
