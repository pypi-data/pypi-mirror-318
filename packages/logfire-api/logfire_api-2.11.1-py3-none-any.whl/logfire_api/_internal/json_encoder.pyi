from .utils import JsonValue as JsonValue, safe_repr as safe_repr
from _typeshed import Incomplete
from typing import Any

NUMPY_DIMENSION_MAX_SIZE: int
EncoderFunction: Incomplete

def encoder_by_type() -> dict[type[Any], EncoderFunction]: ...
def to_json_value(o: Any, seen: set[int]) -> JsonValue: ...
def logfire_json_dumps(obj: Any) -> str: ...
def is_sqlalchemy(obj: Any) -> bool: ...
def is_attrs(cls) -> bool: ...
