"""layer"""
from typing import(
    Any,
    Dict)
from http.client import (
    BAD_REQUEST,
    CREATED,
    OK,
    SERVICE_UNAVAILABLE)


def lambda_response(status_code: (BAD_REQUEST|CREATED|OK|SERVICE_UNAVAILABLE)) -> Dict[str, Any]:
    """lambda_response"""
    return {"status_code": status_code}


def lambda_response_created() -> Dict[str, Any]:
    """lambda_response_created"""
    return lambda_response(CREATED)


def lambda_response_ok() -> Dict[str, Any]:
    """lamdba_response_ok"""
    return lambda_response(OK)

def hello(
        name: str) -> None:
    """hello"""
    print(f"Hello {name}!")

def world(world: str) -> None:
    hello(world)