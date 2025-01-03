"""
Built in theme objects for bprint
"""

from types import NoneType, FunctionType
from typing import Final

from .colors import rgb, RESET
from .packing import pepr
from .theme import Theme, add_theme

BLAND: Final[Theme] = add_theme(Theme("bland"))
"""A bland, colorless theme but provides nice formatting. Like pprint's theme"""


@BLAND.packer(cls=dict)
def _pack_dict(_value: dict):
    ret = '{'

    for i, (k, v) in enumerate(_value.items()):
        ret += f"{pepr(k)}: {pepr(v, strip=True)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += '}'
    return ret


@BLAND.packer(cls=list)
def _pack_list(_value: list):
    ret = '['

    for i, v in enumerate(_value):
        ret += f"{pepr(v)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += ']'

    return ret


@BLAND.packer(cls=tuple)
def _pack_tuple(_value: tuple):
    if len(_value) == 1:
        return repr(_value)

    ret = '('

    for i, v in enumerate(_value):
        ret += f"{pepr(v)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += ')'

    return ret


DEFAULT: Final[Theme] = add_theme(Theme("default"))
"""The default bprint theme. Nice colors inspired by PyCharm's dark theme"""


# It's not the exact same since the colors were chosen using the power-toys color picker, not by digging in the source code


@DEFAULT.packer(cls=str)
def _pack_str(_value: str):
    return f"{rgb(92, 170, 91)}{_value!r}{RESET}"


@DEFAULT.packer(cls=int)
def _pack_int(_value: int):
    return f"{rgb(39, 146, 177)}{_value}{RESET}"


@DEFAULT.packer(cls=float)
def _pack_float(_value: float):
    return f"{rgb(39, 146, 177)}{_value}{RESET}"


@DEFAULT.packer(cls=bool)
def _pack_bool(_value: bool):
    return f"{rgb(203, 139, 107)}{_value}{RESET}"


@DEFAULT.packer(cls=NoneType)
def _pack_none(_value: NoneType):
    return f"{rgb(203, 139, 107)}{_value}{RESET}"


@DEFAULT.packer(cls=dict)
def _pack_dict(_value: dict):
    ret = '{'

    for i, (k, v) in enumerate(_value.items()):
        if isinstance(k, str):
            # So that we can print keys that are strings in a different color
            k = f"{rgb(197, 122, 182)}\n\t{k!r}{RESET}"
        else:
            k = pepr(k)

        ret += (f"{k}: "
                f"{pepr(v, strip=True)}")

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += '}'
    return ret


@DEFAULT.packer(cls=FunctionType)
def _pack_function(_value: FunctionType):
    return f"{rgb(84, 163, 242)}{_value.__name__}{RESET}({', '.join(f"{arg}: {rgb(99, 117, 186)}{tp.__name__}{RESET}" for arg, tp in _value.__annotations__.items())})"


# You can add packers without using a decorator like so:
DEFAULT.packer(cls=tuple)(_pack_tuple)
DEFAULT.packer(cls=list)(_pack_list)
