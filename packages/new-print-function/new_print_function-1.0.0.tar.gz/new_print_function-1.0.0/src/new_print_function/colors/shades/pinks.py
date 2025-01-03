PINKS = {
    "pink": {
        "fg": "\033[38;2;255;192;203m",
        "bg": "\033[48;2;255;192;203m",
    },
    "light-pink": {
        "fg": "\033[38;2;255;182;193m",
        "bg": "\033[48;2;255;182;193m",
    },
    "hot-pink": {
        "fg": "\033[38;2;255;105;180m",
        "bg": "\033[48;2;255;105;180m",
    },
    "deep-pink": {
        "fg": "\033[38;2;255;20;147m",
        "bg": "\033[48;2;255;20;147m",
    },
    "medium-violet-red": {
        "fg": "\033[38;2;199;21;133m",
        "bg": "\033[48;2;199;21;133m",
    },
    "pale-violet-red": {
        "fg": "\033[38;2;219;112;147m",
        "bg": "\033[48;2;219;112;147m",
    },
}

if __name__ == "__main__":
    for color, ansi_code in PINKS.items():
        print(f"{ansi_code["fg"]}This is {color} foreground.\033[0m")
        print(f"{ansi_code["bg"]}This is {color} background.\033[0m")
