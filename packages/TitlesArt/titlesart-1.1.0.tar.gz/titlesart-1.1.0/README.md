# TitlesArt

TitlesArt is a Python library that makes it easy to create artistic titles for command-line tools. With this library, you can convert text into visually appealing ASCII art, which can be used as headers or titles in your terminal-based applications.

## Installation

To use TitlesArt, you can install it directly in your Python environment. If you're using a virtual environment (which is highly recommended), install the dependencies by running:

```bash
pip install -r requirements.txt
pip install titlesart
```

## Usage

### 1. Importing the Library:
You can use the library by importing the titles_art module and calling the appropriate functions.
```bash
from titles_art import main

# Text you want to convert into ASCII art
text = "HELLO WORLD"

# Convert the text into its ASCII art representation
ascii_art = main.textToCol(text)

# Print the ASCII art
main.printText(ascii_art)
```

### 2. Available Functions:

- textToCol(text): Converts the input text into a list of ASCII art representations.
- printText(text_arrays): Prints the ASCII art in a readable format on the console.

## Example

Here is a simple example of how to use the library to create and print a title:
```bash
from titles_art import main

text = "hello world"
ascii_art = main.textToCol(text)
main.printText(ascii_art)
```
## Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b new-feature.
3. Make your changes and commit them: git commit -am 'Add new feature'.
4. Push to your forked repository: git push origin new-feature.
5. Open a Pull Request to propose your changes.
