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

## `get_encoding()`, `get_max_line_length()`, `get_line_ending()`, `get_indent_size()`

Given a .editorconfig file as a dict (from `get_config()`), these methods will return the encoding, max line length, or line ending as a str or int but will also return None if they are not specified in the configuration file.

| Argument | Type | Description |
| --- | --- | --- |
| `config` | `dict` | The configuration file as a dict. |

## `glob_match()`, `parse_file(), `get_bool()`

These methods are used internally to match the globs in the configuration file and convert the strings in the configuration file to booleans.

## `LineEnding` and `Section` classes

These classes are used internally to represent the line endings and sections in the configuration file.
## Example:

```python
from os import path

from pyeditorconfig import get_config

print(get_config(__file__)) # Assumes that there is a .editorconfig file in the same directory as this file
# This prints the editorconfig for the examples.py file
```