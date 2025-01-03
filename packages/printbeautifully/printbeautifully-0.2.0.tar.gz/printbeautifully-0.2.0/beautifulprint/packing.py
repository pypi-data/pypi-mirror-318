from types import FunctionType

from .theme import current_theme


def packer(cls: type):
    return current_theme().packer(cls)


def bepr(obj: object, *, default: FunctionType = repr) -> str:
    """
    Like repr, but better; beautiful repr! Uses pepr internally.
    """
    ret = pepr(obj, default=default)

    # Remove the starting newline
    ret = ret[1:]

    # Unindent by 1
    split = ret.splitlines()
    ret = ''
    for i, line in enumerate(split):
        ret += line[1:]

        # Don't add trailing newline
        if i < len(split) - 1:
            ret += '\n'

    return ret


def pepr(obj: object, *, default: FunctionType = repr, strip: bool = False) -> str:
    """
    Inner bepr function used for packer functions. Calls the packer function of the object's type on the object.
    "It needs more pepr, Mason."
    """

    if type(obj) in current_theme():
        data: str = current_theme()[type(obj)](obj)
    else:
        data: str = default(obj)

    # You have to add a blank item at the start so all lines are indented uniformly
    lines = [''] + data.splitlines()

    ret = ''
    for i, line in enumerate(lines):
        if i > 0:
            ret += '\t'

        ret += line

        if i < len(lines) - 1:
            ret += '\n'
    if strip:
        ret = ret.strip()

    return ret

