# Logstore

A simple Python logging package which stores log in memory.

## Installation

```bash
pip install logstore
```

## Usage
```python
from logstore import Logger, DEBUG, INFO

logger = Logger(level=INFO, app="MyApp")
logger.info("This is an info message")
print(logger)

```
## License

```text
MIT License
...