# WhoisQuery

A simple and efficient WHOIS lookup library for Python.

## Installation

```bash
pip install whoisquery
```

## Usage

### As a Library

```python
from whoisquery import WhoisQuery

# Create a WHOIS lookup instance
whois = WhoisQuery("example.com")

#Get WHOIS data
data = whois.execute_whois()

print(data)
```

### As a Command Line Tool

```bash
whoisquery -d example.com
```

## Features

- Performs WHOIS lookups for domain names
- Parses WHOIS output into structured data
- Extracts key information such as:
  - Registration dates
  - Domain status
  - Nameservers
  - Registrar information
  - DNSSEC status

## Requirements

- Python 3.7 or higher
- `whois` command-line tool installed on the system

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G4MDF91)