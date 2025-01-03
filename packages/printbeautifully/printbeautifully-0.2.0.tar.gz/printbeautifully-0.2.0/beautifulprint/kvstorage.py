"""
Storage using a nested list of key-value pairs - like a dictionary but not using a hash table
"""
from __future__ import annotations

from typing import Any, Self


class KVStorage:
    """
    Behaves almost the same as a dict, but it does not use hashing
    """
    def _pack(self) -> str:
        ret = '{'
        for k, v in self._storage:
            ret += f"{k!r}: {v!r}, "

        ret += '}'
        return ret

    def __repr__(self):
        return f"{self.__class__.__name__}.from_dict({self._pack()})"

    def __init__(self):
        self._storage: list[list[Any, Any]] = []

    def to_dict(self) -> dict[Any, Any]:
        """
        Attempt to convert to a regular dict
        """
        return {k: v for k, v in self.items()}

    @classmethod
    def from_dict(cls, data: dict[Any, Any]) -> Self:
        self = cls()
        for k, v in data.items():
            self[k] = v

        return self

    def keys(self) -> list[Any]:
        return [k for k, _ in self._storage]

    def values(self) -> list[Any]:
        return [v for _, v in self._storage]

    def items(self) -> zip:
        return zip(self.keys(), self.values())

    def __contains__(self, item):
        return item in self.keys()

    def __setitem__(self, key: Any, value: Any) -> None:
        for i, item in enumerate(self._storage):
            if item[0] == key:
                self._storage[i][1] = value
                break
        else:
            # `else` clause is run if the for loop exits without a `break`
            self._storage.append([key, value])

    def __getitem__(self, key):
        for _key, _value in self.items():
            if _key == key:
                return _value

        raise KeyError(key)

    def get(self, key: Any, default: Any = None) -> Any:
        if key in self:
            return self[key]
        else:
            return default
