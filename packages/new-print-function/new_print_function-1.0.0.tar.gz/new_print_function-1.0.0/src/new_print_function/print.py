from typing import Any, Optional, TextIO
from .format import format, ANSI_RESET_CODE
from .literals import SUPPORTED_COLORS, SUPPORTED_FONT_STYLES

echo = print

def print(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    file: Optional[TextIO] = None,
    flush: bool = False,
    fg: Optional[SUPPORTED_COLORS] = None,
    bg: Optional[SUPPORTED_COLORS] = None,
    fs: Optional[SUPPORTED_FONT_STYLES] = None,
):
    if any((fg, bg, fs)):
        objects = tuple(format(f"{obj}", fg, bg, fs, reset=False) for obj in objects)
        if end.endswith("\n"):
            end = end.rstrip("\n")
            end += ANSI_RESET_CODE + "\n"  # Reset before newline character
        else:
            end += ANSI_RESET_CODE
    echo(*objects, sep=sep, end=end, file=file, flush=flush)
