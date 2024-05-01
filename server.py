import os
from importlib import import_module
from os.path import basename
from redis_om import Migrator
from starlette.applications import Starlette
from strawberry.asgi import GraphQL
from src.models.bot.user_bot import UserBot
from src.models.user.user_roles import UserRoles
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
# Migrator(os.path.abspath(os.path.join(__file__, "src", "models", "server"))).run()
# Migrator(os.path.abspath(os.path.join(__file__, "src", "models", "bot"))).run()
# Migrator(UserRoles).run()
# Migrator(UserBot).run()


## usage:
## 1) create the docker network layer:
##  $ docker create network network-backend
## 2) start docker containers and attaching them to the
## created network:
##  $ docker run -d --name redis-container --network=network-backend
##    --publish=6379:6379 redis/redis-stack:latest
## 3) start backend container:
##  $ docker run -d --name backend-container --network=network-backend
##    --publish=8000:8000  -v .:/app bot-backend
##


# uvicorn server:app
