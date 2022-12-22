from dataclasses import dataclass

import strawberry


@dataclass
@strawberry.type
class Estate:
    _id: strawberry.ID  # strawberry.ID
    title: str
    realtor: str
    description: str
    price: float
    address: str
    parking_spaces: int
    furnished: bool
    other_costs: float | None = None
    created_on: str | None = None
    last_updated_on: str | None = None

    @property
    def id(self) -> strawberry.ID:  # strawberry.ID:
        return self._id


@dataclass
@strawberry.input
class EstateIn:
    title: str
    realtor: str
    description: str
    price: float
    address: str
    parking_spaces: int
    furnished: bool
    other_costs: float | None = None
    created_on: str | None = None
    last_updated_on: str | None = None
