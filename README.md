# QR Code Generator

A simple and efficient Python command-line tool to generate QR codes from text or URLs. This project ensures valid input and produces high-quality PNG images.

## Features

- **Easy to Use**: Simple command-line interface.
- **Input Validation**: Checks for empty strings and size limits to ensure valid QR codes.
- **Safe File Handling**: Automatically sanitizes filenames and ensures correct extensions.
- **High Quality**: Generates standard PNG QR codes using the `qrcode` library.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zoro-sishui/QR-Generator.git
   cd QR-Generator
   ```

2. **Set up a virtual environment (Recommended)**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the terminal using `main.py`.

### Basic Usage
Generate a QR code for a URL or text. The default output file is `qr_code.png`.

```bash
python3 main.py --data "https://www.example.com"
```

### Custom Output Filename
Specify a custom filename for the generated image.

```bash
python3 main.py --data "Hello World" --output "my_message.png"
```

## Running Tests

The project includes a suite of unit tests to ensure reliability.

1. **Configure Environment**
   The project uses a `.env` file to handle python paths for testing.
   ```bash
   echo "PYTHONPATH=." > .env
   ```

2. **Run Tests**
   ```bash
   export $(cat .env | xargs) && python3 -m unittest discover tests
   ```
   *Note: If you are using VS Code, the tests should be discovered automatically.*

## Project Structure

```
.
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
├── src/
│   └── qr_generator/
│       ├── generator.py    # QR code generation logic
│       ├── validator.py    # Input validation logic
│       └── utilis.py       # File path and string utilities
└── tests/
    └── test_qr_generator.py # Unit tests
```

## Technologies Used

- [Python](https://www.python.org/)
- [qrcode](https://pypi.org/project/qrcode/) - For generating QR code images.
- [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library support.

