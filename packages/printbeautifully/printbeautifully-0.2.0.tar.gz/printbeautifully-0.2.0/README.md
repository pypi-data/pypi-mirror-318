# beautifulprint

---

Pretty print, but it's prettier than pretty print (because it's colorized!)

Run `pip install printbeautifully`

Beautifulprint is a light-weight python package that allows you to easily and simply print data in a nice format. It
also has strong customisation using function decorators and theme objects.

Note: it does not yet support self-referencing dictionaries/tuples

## Helpful links

- [PyPI project](https://pypi.org/project/printbeautifully/0.1.1/)
- [GitHub repo](https://github.com/FAReTek1/beautifulprint/)

## Usage

- Print a builtin data structure:
```py
from beautifulprint import bprint

bprint({
    "key": "value",
    "number_list": [1, 2, 3],
    "it also supports tuples!": (True, None, False)
})
```

- Print multiple pieces of data:
```py
from beautifulprint import bprint

bprint({
    "key": "value",
    "number_list": [1, 2, 3],
    "it also supports tuples!": (True, None, False)
}, # Just use a comma!
["a", "b", "c", 123.456] 
  )
```

- Use a different theme:
```py
from beautifulprint import bprint, themes

with themes.BLAND: # You use a with statement
  bprint({
    "key": "value",
    "number_list": [1, 2, 3],
    "it also supports tuples!": (True, None, False)
  })
```

- Or make your own theme:
```py
from beautifulprint import bprint, Theme, pepr, rgb, RESET

my_theme = Theme("my cool theme")  # Name of theme. Just used for printing the theme object


@my_theme.packer(cls=dict)  # This decorator registers this function to my_theme as a way to format/pack a dictionary
def pack_dict(value: dict) -> str:
    # This method will only be passed a dict (because of the decorator above) and must return a string
    ret = 'dict('
    for key, value in value.items():
        # You use pepr, which will handle formatting child objects.
        # You handle coloring in here as well, with the rgb function. You can also you colorama if you want
        ret += f"{rgb(255, 0, 255)}{pepr(key)}{RESET} = {rgb(0, 255, 0)}{pepr(value, strip=True)}{RESET}, "
        # The value item shouldn't be placed on a newline, so we strip the whitespace
    ret += '\n)'

    return ret


with my_theme:  # You use a with statement
    bprint({
        "key": "value",
        "number_list": [1, 2, 3],
        "it also supports tuples!": (True, None, False)
    })

```