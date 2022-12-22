import strawberry
from strawberry.fastapi import GraphQLRouter

from src.estates.models import Estate
from src.estates.resolver import create_estate, find_estates


@strawberry.type
class Query:
    find_all_estates: list[Estate] = strawberry.field(resolver=find_estates)


@strawberry.type
class Mutation:
    new_estate: Estate = strawberry.field(resolver=create_estate)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
