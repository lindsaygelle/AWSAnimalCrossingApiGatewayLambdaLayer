"""http"""
import uuid
from datetime import date, datetime
from http.client import BAD_REQUEST, CREATED, OK, UNAUTHORIZED, SERVICE_UNAVAILABLE
from typing import AnyStr, Literal, Optional, TypedDict, TypeVar

MethodTypeT = TypeVar("MethodTypeT", Literal["GET"], Literal["PATCH"], Literal["POST"])


class LinkTypeT(TypedDict):
    """LinkTypeT"""

    http_method: MethodTypeT
    href: str
    rel: str


class BaseTypeT(TypedDict):
    """LinkTypeT"""

    id: (int | str)
    link: LinkTypeT
    resource: AnyStr


class BaseDetailTypeT(BaseTypeT):
    """DetailTypeT"""

    created_at: (date | datetime)
    timezone: Optional[str]
    updated_at: (date | datetime)


class BaseResponseTypeT(TypedDict):
    """ResponseTypeT"""

    request_epoch: int
    request_id: uuid.UUID
    response_epoch: int
    response_id: uuid.UUID
    status_code: (BAD_REQUEST | CREATED | OK | UNAUTHORIZED | SERVICE_UNAVAILABLE)
