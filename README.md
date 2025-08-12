# DaySpan

[![PyPI](https://img.shields.io/pypi/v/dayspan?color=%232EA51B&cacheSeconds=300)](https://pypi.org/project/dayspan/)
[![Python Support](https://img.shields.io/pypi/pyversions/dayspan.svg)](https://pypi.org/project/dayspan/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python package to calculate the number of days between two dates (inclusive).

## Features

- Calculate days between two dates, including both start and end dates
- Simple command-line interface
- Cross-platform support (Linux, macOS, Windows)
- No external dependencies - uses only Python standard library
- Clear output indicating inclusive calculation
- Support for dates from year 1 to 9999

## Installation

### From PyPI

```bash
pip install dayspan
```

### From GitHub

```bash
pip install git+https://github.com/YOUR_USERNAME/dayspan.git
```

### From source

```bash
git clone https://github.com/YOUR_USERNAME/dayspan.git
cd dayspan
pip install .
```

### For development

```bash
git clone https://github.com/YOUR_USERNAME/dayspan.git
cd dayspan
pip install -e .
```

## Usage

### Command Line Interface

Basic usage:
```bash
dayspan 20250101 20251231
```

Output:
```
365 days (from 2025-01-01 to 2025-12-31, inclusive)
```

Verbose output:
```bash
dayspan -v 20250101 20251231
```

Output:
```
Start date: 2025-01-01
End date: 2025-12-31
Days from 2025-01-01 to 2025-12-31 (inclusive): 365 days
```

Help:
```bash
dayspan -h
```

Version:
```bash
dayspan --version
```

### Python API

```python
from dayspan import calculate_days

# Calculate days between two dates
days, start_formatted, end_formatted = calculate_days("20250101", "20251231")
print(f"{days} days from {start_formatted} to {end_formatted}")
# Output: 365 days from 2025-01-01 to 2025-12-31

# Parse individual dates
from dayspan import parse_date
date = parse_date("20250101")
print(date)  # 2025-01-01 00:00:00
```

## Examples

### Days in a month
```bash
dayspan 20250301 20250331
# Output: 31 days (from 2025-03-01 to 2025-03-31, inclusive)
```

### Days in a leap year
```bash
dayspan 20240101 20241231
# Output: 366 days (from 2024-01-01 to 2024-12-31, inclusive)
```

### Days between two specific dates
```bash
dayspan 19930101 20241231
# Output: 11687 days (from 1993-01-01 to 2024-12-31, inclusive)
```

### Single day
```bash
dayspan 20250101 20250101
# Output: 1 days (from 2025-01-01 to 2025-01-01, inclusive)
```

### Leap year February
```bash
dayspan 20240201 20240229
# Output: 29 days (from 2024-02-01 to 2024-02-29, inclusive)
```

## Why Inclusive?

DaySpan counts both the start and end dates, which is the intuitive way most people think about date ranges:

- From January 1 to January 31 = 31 days (the entire month)
- From Monday to Friday = 5 days (the work week)
- From today to today = 1 day (not 0)

This matches how we naturally count days on a calendar.

## Input Format

- Dates must be in `YYYYMMDD` format
- Year: 0001-9999
- Month: 01-12
- Day: 01-31 (validated according to month and year)

## Error Handling

The tool validates input dates and provides clear error messages:

```bash
# Invalid date format
dayspan 2025-01-01 2025-12-31
# Error: Invalid date format: '2025-01-01'. Expected YYYYMMDD format.

# End date before start date
dayspan 20251231 20250101
# Error: End date (20250101) must be after or equal to start date (20251231)

# Invalid date
dayspan 20250132 20251231
# Error: Invalid date: '20250132'. day is out of range for month
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## Development

### Running Tests

```bash
# Option A
python test_dayspan.py

# Option B
pytest test_dayspan.py
```

### Building from Source

```bash
# Install build tools
pip install build

# Build distributions
python -m build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Cong Gao - [cnggao@gmail.com](mailto:cnggao@gmail.com)

## Acknowledgments

- Thanks to all contributors who have helped with this project
- Inspired by the need for a simple, reliable day calculation tool

## Changelog

### v1.0.5 (2025-08-12)
- update the pip badge

### v1.0.4 (2025-08-12)
- builded by .toml instead of setup.py

### v1.0.3 (2025-07-03)
- Initial release
- Basic day calculation functionality
- Command-line interface
- Python API
- Cross-platform support

---

If you find this tool useful, please consider giving it a star on [GitHub](https://github.com/CongGao-CG/dayspan)!
