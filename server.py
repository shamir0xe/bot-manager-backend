from redis_om import Migrator
from starlette.applications import Starlette
from strawberry.asgi import GraphQL
from src.facades.env import Env
from src.api.schema import schema
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware

# from src.policies.authentication import GuardAuthHandler


graphql_app = GraphQL(schema)
middleware = [
    Middleware(SessionMiddleware, secret_key=Env().session_key),
    Middleware(CORSMiddleware, allow_origins=["*"]),
]
app = Starlette(debug=Env().debug, middleware=middleware)
app.mount("/api", graphql_app)
Migrator().run()

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
