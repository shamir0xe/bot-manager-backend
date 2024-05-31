from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from src.actions.utility.get_current_time import GetCurrentTime


class AlchBase(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        index=True, doc="Creation Time", default=GetCurrentTime.get
    )
    updated_at: Mapped[datetime] = mapped_column(
        index=True,
        doc="Last Update Time",
        default=GetCurrentTime.get,
        onupdate=GetCurrentTime.get,
    )
