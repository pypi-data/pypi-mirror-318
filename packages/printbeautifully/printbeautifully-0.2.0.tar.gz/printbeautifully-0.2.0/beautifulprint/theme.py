from __future__ import annotations

from types import FunctionType

from beautifulprint.kvstorage import KVStorage

theme_stack: list[Theme] = []


def current_theme() -> Theme:
    return theme_stack[-1]


def add_theme(theme: Theme) -> Theme:
    theme_stack.append(theme)
    return theme


def pop_theme() -> Theme:
    return theme_stack.pop()


class Theme:
    """
    Object with its own packer function storage
    """

    def __init__(self, name: str = None):
        self._store = KVStorage()
        self.name = name

    def __repr__(self):
        return f"<Theme {self.name}>"

    def __enter__(self):
        add_theme(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pop_theme()
        return False

    def __contains__(self, item):
        return item in self._store

    def __getitem__(self, item):
        return self._store[item]

    def __setitem__(self, key, value):
        self._store[key] = value

    def packer(self, cls: type):
        def decorator(func: FunctionType):
            # print(f"Registering {cls} packer with {func}")
            self[cls] = func

            return func

        return decorator

