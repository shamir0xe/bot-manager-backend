from datetime import datetime, timedelta
from src.helpers.config.config import Config


class DatetimeDelegator:
    @staticmethod
    def valid_due_date(expiration_date: datetime) -> bool:
        return datetime.now() < expiration_date

    @staticmethod
    def expiration_from_now() -> datetime:
        return datetime.now() + DatetimeDelegator.expiration_duration()

    @staticmethod
    def expiration_duration() -> timedelta:
        return timedelta(minutes=Config.read("token.expiration_duration"))
