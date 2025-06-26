import strawberry
from fastapi import APIRouter
from strawberry.fastapi import GraphQLRouter

from .model import Query

schema = strawberry.Schema(query=Query)


# APIルータ
router = APIRouter()
graphql_app = GraphQLRouter(schema)

router.include_router(
    graphql_app, prefix="/GraphQLSample/graphql", include_in_schema=False)
