# Fire and Security Alarm Monitoring System (FASAM)

This project implements a Fire and Security Alarm Monitoring System (FASAM) for a large building. The system monitors and controls all fire and security alarms in the building, ensuring appropriate actions are taken based on the detected conditions.

## Features

- Smoke detection and confirmation
- Activation of alarms, sprinklers, and emergency lighting
- Automatic calling of emergency services
- Handling of power failures
- Incident report generation

## Project Structure

FASAM/
├── src/
│ ├── main.py
│ ├── control_area.py
├── tests/
│ ├── test_control_area.py
├── README.md
├── requirements.txt

### Directory and File Breakdown

- **FASAM/**: Root directory of the project.
- **src/**: Source code directory.
  - **main.py**: The main script to run the application.
  - **control_area.py**: Contains the refactored `ControlArea` class and its methods.
- **tests/**: Directory for test files.
  - **test_control_area.py**: Contains the `unittest` test cases for the `ControlArea` class.
- **README.md**: Project description, setup instructions, and documentation.
- **requirements.txt**: List of dependencies.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/FASAM.git
   cd FASAM

   ```

2. Install the dependencies
   pip install -r requirements.txt

## Usage

1. Navigate to the src directory:
   cd src
2. Run the main script:
   python main.py

## Running Test

1. Navigate to the tests directory:
   cd tests
2. Run the test cases:
   python -m unittest test_control_area.py

## Contributing

    Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

    This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

    For questions or suggestions, please open an issue or contact your-email@example.com.
