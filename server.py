from contextlib import asynccontextmanager
from redis_om import Migrator
from src.actions.database.run_seeders import RunSeeders
from src.facades.env import Env
from src.api.schema import schema
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    RunSeeders.run()
    yield


graphql_app = GraphQLRouter(schema)
app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=Env().session_key)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
app.include_router(graphql_app, prefix="/api")

Migrator().run()

