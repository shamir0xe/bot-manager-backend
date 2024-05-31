import functools
from src.facades.local_repository.database_engine import DatabaseEngine
from src.actions.database.create_database_session import CreateDatabaseSession


def db_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        engine = DatabaseEngine().engine
        session = CreateDatabaseSession.create(engine)
        kwargs["session"] = session
        result = func(*args, **kwargs)
        session.commit()
        session.close()
        return result

    return wrapper
