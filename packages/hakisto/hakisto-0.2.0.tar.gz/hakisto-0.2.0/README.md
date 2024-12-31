# Hakisto

The name: **Hakisto** means Logger in Esperanto.

## Logging reimagined...

## Simple...

```python
from hakisto import logger

logger.warning('something is fishy...')
```

Starts logging to console and file.

### Example output

```
hakisto-demo-color
```

![](https://gitlab.com/hakisto/logger/-/raw/main/docs/images/demo-color.png)

```
hakisto-demo-critical
```

![](https://gitlab.com/hakisto/logger/-/raw/main/docs/images/demo-critical.png)

```
hakisto-demo-traceback
```

![](https://gitlab.com/hakisto/logger/-/raw/main/docs/images/demo-traceback.png)

## Installation

```
pip install hakisto
```

or get the source from [gitlab.com/hakisto/logger](https://gitlab.com/hakisto/logger/).

## Documentation

[Read the Docs](https://hakisto.readthedocs.io)

## Changes

| Version | Changes                                                                   |
|---------|---------------------------------------------------------------------------|
| `0.2.0` | Add `set_date_format()` to `Logger` and `logger`.                         |
| `0.1.1` | No functional changes, just making **README** and **Read the Docs** work. |
