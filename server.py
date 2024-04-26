from redis_om import Migrator
from starlette.applications import Starlette
from strawberry.asgi import GraphQL
from src.facades.env import Env
from src.api.schema import schema
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

# from src.policies.authentication import GuardAuthHandler


graphql_app = GraphQL(schema)
middleware = [Middleware(SessionMiddleware, secret_key=Env().session_key)]
app = Starlette(debug=Env().debug, middleware=middleware)
app.mount("/api", graphql_app)
Migrator().run()

# usage:
# uvicorn server:app
