# image-to-ascii

A toy project that converts images to ASCII art on the terminal.

## Features

- Convert JPG, PNG, and other formats to ASCII
- Adjustable width and height for output size
- CLI interface for easy usage

## How to use

1. Clone the repo into your machine:
```bash
git clone https://github.com/andrew-carvalho/image-to-ascii.git
```

2. Move to project directory
```bash
cd image-to-ascii
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

4. Execute the program with python in your terminal passing the image path:
```bash
python app/main.py example.jpg
```

## Options

- `-h` or `--help`: Display program's help information
- `-wt` or `--width`: Change the output width
- `-ht` or `--height`: Change the output height