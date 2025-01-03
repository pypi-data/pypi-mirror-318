from typing import Optional
from .colors import COLORS
from .font_styles import FONT_STYLES
from .literals import SUPPORTED_COLORS, SUPPORTED_FONT_STYLES

ANSI_RESET_CODE = "\033[0m"


def format(
    text: str,
    fg: Optional[SUPPORTED_COLORS] = None,
    bg: Optional[SUPPORTED_COLORS] = None,
    fs: Optional[SUPPORTED_FONT_STYLES] = None,
    reset: bool = True,
) -> str:
    fg_color = COLORS.get(fg, {}).get("fg", "")
    bg_color = COLORS.get(bg, {}).get("bg", "")
    font_style = FONT_STYLES.get(fs, "")

    return fg_color + bg_color + font_style + text + (ANSI_RESET_CODE if reset else "")
