# VSOpen

A simple command-line tool to clone GitHub repositories and open them in VS Code.

## Installation

### From PyPI (recommended):
```bash
pip install vsopen
```

### From GitHub:
```bash
pip install git+https://github.com/frenzywall/vsopen.git

git clone https://github.com/frenzywall/vsopen.git
cd vsopen
pip install .
```

## Usage

```bash
vsopen https://github.com/username/repository.git
```

Or simply run:

```bash
vsopen
```

And enter the GitHub URL when prompted.

## Development
To contribute:
1. Fork the repository
2. Clone your fork
3. Install development dependencies:
```bash
pip install -e .
```

## License
MIT License
