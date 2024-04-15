from blacksheep import Application
from strawberry.asgi import GraphQL
from src.api.schema import schema


app = Application()
graphql_app = GraphQL(schema)
app.mount("/api", graphql_app)
