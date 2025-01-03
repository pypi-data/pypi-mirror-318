"""
Old version of beautifulprint for legacy use
"""

CSI = '\033['


def code_to_chars(code):
    # This code is from the colorama module.
    # Included here, so you don't need to import all of colorama
    return CSI + str(code) + 'm'


class Theme:
    def __init__(self, mode: str = "code_to_chars", **kwargs):
        self.theme = kwargs
        for color, value in self.theme.items():
            if color == "METHODS":
                raise ValueError(
                    "Color cannot be called 'METHODS'"
                )
            if mode == "code_to_chars":
                self.__setattr__(color, code_to_chars(value))
            else:
                self.__setattr__(color, value)

        self.METHODS = {}

    def get(self, key):
        return self.__dict__.get(key)


class DictionaryObject(dict):
    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self[key] = value


# Color codes taken from colorama.fore
colors = (DictionaryObject(
    BLACK=30,
    RED=31,
    GREEN=32,
    YELLOW=33,
    BLUE=34,
    MAGENTA=35,
    CYAN=36,
    WHITE=37,
    RESET=39,
    LIGHTBLACK_EX=90,
    LIGHTRED_EX=91,
    LIGHTGREEN_EX=92,
    LIGHTYELLOW_EX=93,
    LIGHTBLUE_EX=94,
    LIGHTMAGENTA_EX=95,
    LIGHTCYAN_EX=96,
    LIGHTWHITE_EX=97,
))

default_theme = Theme(
    RESET=colors.RESET,

    NUM=colors.BLUE,
    STR=colors.GREEN,
    FUNC=colors.CYAN,
    BOOL=colors.BLUE,
)


def type_name(obj) -> str:
    return type(obj).__name__


ITERABLES = [
    "list",
    "dict",
    "tuple"
]


def bprint(*args, theme: Theme = default_theme, end: str = '\n'):
    if len(args) == 1:
        bprint_inner(args[0], theme, end)
    else:
        for i, arg in enumerate(args):
            if i == len(args) - 1:
                bprint_inner(arg, theme, end)
            else:
                bprint_inner(arg, theme, f"{theme.RESET},\n")


def bprint_inner(obj, theme: Theme = default_theme, end: str = '', tab_level=0, prefix: bool = True):
    tabs = tab_level * '\t'
    if prefix:
        print(tabs, end='')
    match type_name(obj):
        # Used type_name() instead of isinstance() so we can detect functions
        case "float" | "int" | "object":
            print(f"{theme.NUM}{obj}{theme.RESET}", end=end)

        case "function" | "type":
            print(f"{theme.FUNC}{obj.__name__}{theme.RESET}", end=end)

        case "str":
            print(f"{theme.STR}\"{obj}\"{theme.RESET}", end=end)

        case "bool":
            print(f"{theme.BOOL}{obj}{theme.RESET}", end=end)

        case "list" | "tuple":
            if type_name(obj) == "list":
                brackets = "[]"
            else:
                brackets = "()"
            print(brackets[0])
            for i, item in enumerate(obj):
                if i == len(obj) - 1:
                    item_end = '\n'
                else:
                    item_end = ",\n"

                bprint_inner(item, theme=theme, end=item_end, tab_level=tab_level + 1)
            print(f"{tabs}{brackets[1]}", end=end)

        case "dict":
            print('{')
            # print the key (should be a string) with end=": " and then the value as usual but without prefix
            for i, item in enumerate(obj):
                bprint_inner(item, theme=theme, end=f"{theme.RESET}:\t", tab_level=tab_level + 1)

                if i == len(obj) - 1:
                    item_end = "\n"
                else:
                    item_end = ",\n"

                bprint_inner(obj.get(item), end=item_end, tab_level=tab_level + 1, prefix=False)
            print(tabs + "}", end=end)

        case _:
            potential_color = theme.get(type_name(obj).upper())
            potential_method = theme.get("METHODS").get(type_name(obj).upper())
            if potential_method is None:
                if potential_color is None:
                    print(f"{theme.RESET}{obj}", end=end)
                else:
                    print(f"{potential_color}{obj}", end=end)
            else:
                new_format = potential_method(obj)
                if potential_color is None:
                    print(f"{theme.RESET}{new_format}", end=end)
                else:
                    print(f"{potential_color}{new_format}", end=end)


# Example of how to use custom formatting

# You receive an object (in this case a theme)
# and return a string with a formatted version
def format_theme(theme: Theme) -> str:
    new_format = "Theme("

    for color in theme.theme:
        new_format += f"\n\t{color}: {theme.theme.get(color)}"
    new_format += "\n)"

    new_format += f"\n\tMETHODS: {theme.METHODS}"
    return new_format


# Then make sure to add this custom formatting to the theme that you are using
default_theme.METHODS = {
    "THEME": format_theme
}

# Example usage
if __name__ == "__main__":
    bprint(1234.234234)
    bprint("hello world")
    bprint(bprint)
    bprint(True)

    array = \
        [
            1, 2, "foo", "bar",
            [
                True, False, "hmm"
            ],
            [
                "hah",
                [
                    "huh", False
                ],
                "oops"
            ]
        ]
    bprint(array)

    dictionary = \
        {
            "num": 42,
            "auth": {
                "user": "temp temp23948234u80234b",
                "pass": ""
            },
            "service": {
                "api_url": "oof",
                "identity_service_url": "t",
                "yo": ("you be lucky", "mate")
            }
        }
    bprint(dictionary)

    bprint(
        ("hi", "there")
    )

    bprint(default_theme)
    bprint("hi", "i", "like", 123)

    bprint(Theme)
