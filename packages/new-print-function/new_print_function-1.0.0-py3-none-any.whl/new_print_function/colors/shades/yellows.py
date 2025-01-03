YELLOWS = {
    "gold": {
        "fg": "\033[38;2;255;215;0m",
        "bg": "\033[48;2;255;215;0m",
    },
    "yellow": {
        "fg": "\033[38;2;255;255;0m",
        "bg": "\033[48;2;255;255;0m",
    },
    "light-yellow": {
        "fg": "\033[38;2;255;255;224m",
        "bg": "\033[48;2;255;255;224m",
    },
    "lemon-chiffon": {
        "fg": "\033[38;2;255;250;205m",
        "bg": "\033[48;2;255;250;205m",
    },
    "light-goldenrod-yellow": {
        "fg": "\033[38;2;250;250;210m",
        "bg": "\033[48;2;250;250;210m",
    },
    "papaya-whip": {
        "fg": "\033[38;2;255;239;213m",
        "bg": "\033[48;2;255;239;213m",
    },
    "moccasin": {
        "fg": "\033[38;2;255;228;181m",
        "bg": "\033[48;2;255;228;181m",
    },
    "peach-puff": {
        "fg": "\033[38;2;255;218;185m",
        "bg": "\033[48;2;255;218;185m",
    },
    "pale-goldenrod": {
        "fg": "\033[38;2;238;232;170m",
        "bg": "\033[48;2;238;232;170m",
    },
    "khaki": {
        "fg": "\033[38;2;240;230;140m",
        "bg": "\033[48;2;240;230;140m",
    },
    "dark-khaki": {
        "fg": "\033[38;2;189;183;107m",
        "bg": "\033[48;2;189;183;107m",
    },
}

if __name__ == "__main__":
    for color, ansi_code in YELLOWS.items():
        print(f"{ansi_code["fg"]}This is {color} foreground.\033[0m")
        print(f"{ansi_code["bg"]}This is {color} background.\033[0m")

    for i, color in enumerate(YELLOWS.keys(), start=131):
        print(
            str(i)
            + f'. <p style="background-color: {color.replace("-", "")}; color: black;">{color}</p>'
        )
