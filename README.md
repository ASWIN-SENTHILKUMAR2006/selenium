# Selenium Lab Prototype

This repository contains a simple Selenium try-out developed under guidance during lab classes. It is an educational prototype intended to demonstrate basic browser automation techniques and to serve as a reference for learning.

## Prerequisites
- Python 3.8 or later
- pip
- A modern web browser (Google Chrome or Firefox)
- The appropriate WebDriver for your browser (chromedriver or geckodriver) or use webdriver-manager

## Installation
1. Create and activate a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
2. Install dependencies:
   pip install -r requirements.txt
   # or, if there is no requirements file:
   pip install selenium webdriver-manager

## Running the examples
- Update any driver paths or browser settings in the example scripts if required.
- Run an example script:
  python examples/example_test.py

## Project structure
- examples/    – example Selenium scripts used during the lab
- tests/       – test cases (if present)
- requirements.txt – Python dependencies

## Notes
- This project is a learning prototype and is not intended for production use.
- Browser and WebDriver versions should be compatible; consider using webdriver-manager to simplify driver management.

## Contributing
Contributions and improvements are welcome. Please open an issue or submit a pull request with a clear description of changes.

## License
No license has been specified for this repository. If you would like a license added, tell me which one and I will add it for you.