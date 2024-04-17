from starlette.applications import Starlette
from strawberry.asgi import GraphQL
from src.helpers.config.config import Config
from src.api.schema import schema
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

# from src.policies.authentication import GuardAuthHandler


graphql_app = GraphQL(schema)
middleware = [
    Middleware(SessionMiddleware, secret_key=Config.read("env.session.secret_key"))
]
app = Starlette(debug=True, middleware=middleware)
app.mount("/api", graphql_app)
# app.mount("/api", graphql_app)
# app.use_authentication().add(GuardAuthHandler())
# authorization = app.use_authorization()
# authorization += Policy(
#     AuthenticationMapper.map(AuthenticationTypes.GUARD), AuthenticatedRequirement()
# )
