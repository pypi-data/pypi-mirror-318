import json
from collections.abc import Iterable
from typing import Any, Protocol, Self

import yaml

from pipewine.parsers.base import Parser


class PydanticLike(Protocol):
    @classmethod
    def model_validate(cls, obj: Any) -> Self: ...
    def model_dump(self) -> dict: ...


class JSONParser[T: dict | PydanticLike](Parser[T]):
    def parse(self, data: bytes) -> T:
        json_data = json.loads(data.decode())
        if self._type is None or issubclass(self._type, dict):
            return json_data
        return self._type.model_validate(json_data)

    def dump(self, data: T) -> bytes:
        if isinstance(data, dict):
            json_data = data
        else:
            json_data = data.model_dump()
        return json.dumps(json_data).encode()

    @classmethod
    def extensions(cls) -> Iterable[str]:
        return ["json"]


class YAMLParser[T: str | int | float | dict | list | PydanticLike](Parser[T]):
    def parse(self, data: bytes) -> T:
        yaml_data = yaml.safe_load(data.decode())
        if self._type is None:
            return yaml_data
        elif issubclass(self._type, (str, int, float, dict, list)):
            return self._type(yaml_data)  # type: ignore
        else:
            return self._type.model_validate(yaml_data)

    def dump(self, data: T) -> bytes:
        if isinstance(data, (str, int, float, dict, list)):
            yaml_data = data
        else:
            yaml_data = data.model_dump()
        return yaml.safe_dump(yaml_data).encode()

    @classmethod
    def extensions(cls) -> Iterable[str]:
        return ["yaml", "yml"]
