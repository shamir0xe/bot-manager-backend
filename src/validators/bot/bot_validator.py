import json
from typing import Annotated, List, Optional
from pydantic import BaseModel, BeforeValidator
from .page import Page


def pages_mapper(v: Optional[str]) -> Optional[List[Page]]:
    if not v:
        ## empty pages
        return None
    pages = json.loads(v)
    mapped_pages = []
    if pages and pages["pages"]:
        for page in pages["pages"]:
            mapped_pages += [Page(**page)]
    return mapped_pages


AnnotatedPages = Annotated[Optional[List[Page]], BeforeValidator(pages_mapper)]


class BotValidator(BaseModel):
    """Validate input values with pydantic builtin validators"""

    id: str
    name: str
    token: str
    host: Optional[str]
    port: Optional[int]
    pages: AnnotatedPages
