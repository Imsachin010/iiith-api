# IIITH API

## Overview
This project is a simple API built using FastAPI that provides endpoints for performing basic operations on numbers, such as addition, multiplication, and checking if a number is even or odd.

## Features
- **Addition**: Add two numbers.
- **Multiplication**: Multiply two numbers.
- **Even/Odd Check**: Check if a number is even or odd.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Imsachin010/iiith-api.git
   cd iiith-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. Install the required packages using the setup file:
   ```bash
   pip install -e .
   ```
   This command will automatically install all necessary dependencies defined in the `setup.py` file, making it easy to set up the project on any system.

## Running the Server
To start the server, run the following command:
```bash
uvicorn app.main:app --reload
```

## API Endpoints
- **POST `/add`**: Add two numbers.
  - Request Body: `{"num1": 5, "num2": 3}`
  - Response: `{"operation": "addition", "result": 8}`

- **POST `/multiply`**: Multiply two numbers.
  - Request Body: `{"num1": 4, "num2": 2}`
  - Response: `{"operation": "multiplication", "result": 8}`

- **GET `/check-even-odd`**: Check if a number is even or odd.
  - Query Parameter: `number=7`
  - Response: `{"number": 7, "result": "odd"}`

## License
This project is licensed under the MIT License. 