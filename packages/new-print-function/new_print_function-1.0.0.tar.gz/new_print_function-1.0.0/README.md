
# The New Python Print Function

**The New Python Print Function** is a powerful library that extends Python's built-in `print` function with support for customizable text and background colors, as well as advanced font styles, using ANSI escape sequences.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Function Signatures](#function-signatures)
  - [Using the `print` Function](#using-the-print-function)
  - [Using the `format` Function](#using-the-format-function)
- [Features](#features)
  - [Colors](#colors)
  - [Font Styles](#font-styles)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation

Install via pip:

```bash
pip install new-print-function
```

---

## Usage

The library consists of two main functions: `print` and `format`.

### Function Signatures

#### `format` Function

Applies colors and font styles to a string and returns the styled text.

```python
format(text: str, fg=None, bg=None, fs=None)
```

- `text` (str): The text to format.
- `fg` (str): Foreground color.
- `bg` (str): Background color.
- `fs` (str): Font style.

#### `print` Function

An enhanced version of Python's `print` function, fully compatible with its default parameters while adding support for styles.

```python
print(*objects, sep=' ', end='\n', file=None, flush=False, fg=None, bg=None, fs=None)
```

- Additional Parameters:
  - `fg` (str): Foreground color.
  - `bg` (str): Background color.
  - `fs` (str): Font style.

---

### Using the `print` Function

#### Example Usage

```python
import new_print_function as npf

npf.print("Hello, world!", fg="red", bg="yellow", fs="bold")
```

#### Overriding Built-in `print`

```python
from new_print_function import print

print("Styled text!", fg="blue", fs="underline")
```

---

### Using the `format` Function

```python
import new_print_function as npf

styled_text = npf.format("Hello, world!", fg="green", bg="black", fs="bold")
print(styled_text)
```

---

## Features

### Colors

Supports **140+ colors**, derived from HTML color names, for both foreground and background. Below is a categorized list of supported colors:

#### Blues

- cyan
- aqua
- lightcyan
- paleturquoise
- aquamarine
- turquoise
- mediumturquoise
- darkturquoise
- cadetblue
- steelblue
- lightsteelblue
- powderblue
- lightblue
- skyblue
- lightskyblue
- deepskyblue
- dodgerblue
- cornflowerblue
- mediumslateblue
- royalblue
- blue
- mediumblue
- darkblue
- navy
- midnightblue

#### Reds

- indianred
- lightcoral
- salmon
- darksalmon
- lightsalmon
- crimson
- red
- firebrick
- darkred

#### Greens

- greenyellow
- chartreuse
- lawngreen
- lime
- limegreen
- palegreen
- lightgreen
- mediumspringgreen
- springgreen
- mediumseagreen
- seagreen
- forestgreen
- green
- darkgreen

#### And More...

### Font Styles

Supports **10 font styles**, including:

- bold
- dim
- italic
- underline
- double-underline
- inverse
- hidden
- strikethrough
- frame
- overline

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a branch for your feature or fix.
3. Commit your changes.
4. Open a pull request.

For significant changes, open an issue first to discuss your proposal.

---

## License

The MIT License

Copyright (c) 2025 Haripo Wesley T.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

---

## Author

- **Wesley Tadiwanashe Haripo**  
  - Email: [haripowesleyt@proton.me](mailto:haripowesleyt@proton.me)  
  - GitHub: [haripowesleyt](https://github.com/haripowesleyt)

---
