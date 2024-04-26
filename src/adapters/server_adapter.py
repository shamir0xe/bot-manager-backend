from typing import TYPE_CHECKING, Annotated

import strawberry
from src.adapters.base_adapter import BaseAdapter
from src.models.server.server import Server as ServerModel

if TYPE_CHECKING:
    from src.api.types.server import Server as ServerType


AnnotatedServerType = Annotated["ServerType", strawberry.lazy("src.api.types.server")]


class ServerAdapter(BaseAdapter):
    @staticmethod
    def plug(model: ServerModel) -> AnnotatedServerType:
        if not model.pk:
            raise ValueError("No valid ID is provided")

        data = {
            "id": model.pk,
            "address": model.address,
            "port": model.port,
            "server_ids": model.server_ids or [],
            "owner_id": model.owner_id,
        }

        return ServerType(**data)
