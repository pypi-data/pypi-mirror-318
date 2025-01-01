# Nexius

A powerful Python logging and utility library with colorful output.

## Features

- Colorful logging with multiple log levels
- Customizable output formatting
- Easy-to-use printf-like printing
- Symbol replacements with custom coloring

## Installation

```bash
pip install nexius
```

## Usage

### Logging

```python
from nexius import log

log.info("This is an info message")
log.debug("Debug information")
log.error("An error occurred")
log.warning("Warning message")
log.success("Operation completed successfully")
log.fatal("Fatal error")
```

### Printf

```python
from nexius import printf as print

print("Colorful output with symbols")
print("[test] with (!) and (|) symbols")
```

## Symbols Replacement

Nexius supports automatic symbol replacements:

- `|`: Secondary color
- `->`: Secondary color
- `(+)`: Green symbol
- `($)`: Green symbol
- `(-)`: Red symbol
- `(!)`: Red symbol
- `(~)`: Yellow symbol
- `(#)`: Blue symbol
- `(*)`: Cyan symbol

## License

MIT License

## Author

- **roc4et**
- Email: x@roc4et.de