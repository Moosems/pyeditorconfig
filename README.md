<h1 align="center">pyeditorconfig</h1>

> **Note**
> This module was created by @Akuli due to the lack of maintanence of the normal `editorconfig` module. I simply added it to PyPI and made a few changes to the code. All credit goes to @Akuli.

## Description
This module is a simple implementation of the [EditorConfig](https://editorconfig.org/) file format. It is designed to be simple and easy to use. You use the `get_config()` method with a path as an argument and a dict with the configuration will be returned.


## Installation

`pip install pyeditorconfig`

# Documentation

## `get_config(path)`

This method takes an absolute path as an argument and returns a dict with the configuration. If there is no configuration file, it will return an empty dict.

| Argument | Type | Description |
| --- | --- | --- |
| `path` | `os.path.abspath` or `str` | The absolute path to the file. The str must also be the absolute path or it will not work. |

## Example:

```python
from os import path

from pyeditorconfig import get_config

print(get_config(__file__))
print(get_config(path.abspath("examples.py")))
# Both print the cofig of this file.
```