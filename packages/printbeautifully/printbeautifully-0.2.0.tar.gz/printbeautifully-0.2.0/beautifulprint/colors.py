"""
Simple module supporting 24-bit ANSI RGB color codes. Might only work on Windows...
"""

from typing import Final


# https://stackoverflow.com/questions/15682537/ansi-color-specific-rgb-sequence-bash
def generate_ansi(data: str) -> str:
    return f"\x1b[{data}m"


def rgb(r: int, g: int, b: int) -> str:
    return generate_ansi(f'38;2;{r};{g};{b}')


RESET: Final[str] = generate_ansi('0')
