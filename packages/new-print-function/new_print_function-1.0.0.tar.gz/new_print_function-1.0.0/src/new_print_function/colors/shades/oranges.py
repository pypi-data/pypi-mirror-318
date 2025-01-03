ORANGES = {
    "light-salmon": {
        "fg": "\033[38;2;255;160;122m",
        "bg": "\033[48;2;255;160;122m",
    },
    "coral": {
        "fg": "\033[38;2;255;127;80m",
        "bg": "\033[48;2;255;127;80m",
    },
    "tomato": {
        "fg": "\033[38;2;255;99;71m",
        "bg": "\033[48;2;255;99;71m",
    },
    "orange-red": {
        "fg": "\033[38;2;255;69;0m",
        "bg": "\033[48;2;255;69;0m",
    },
    "dark-orange": {
        "fg": "\033[38;2;255;140;0m",
        "bg": "\033[48;2;255;140;0m",
    },
    "orange": {
        "fg": "\033[38;2;255;165;0m",
        "bg": "\033[48;2;255;165;0m",
    },
}

if __name__ == "__main__":
    for color, ansi_code in ORANGES.items():
        print(f"{ansi_code["fg"]}This is {color} foreground.\033[0m")
        print(f"{ansi_code["bg"]}This is {color} background.\033[0m")
