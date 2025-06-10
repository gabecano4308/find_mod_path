# 🔍 Module Finder

A lightweight Python utility that finds the file path for one or more Python modules and optionally classifies the type of each module (pure Python, package, C extension, built-in).

---

## Funtionality

Given one or more Python module names, this script:

- Imports each module (if available)
- Prints its file location (if it exists)
- Optionally classifies each module as:
  - **Pure Python** (`.py`)
  - **Package** (`__init__.py`)
  - **Compiled C extension** (`.so` or `.pyd`)
  - **Built-in** (no file on disk)

---

## Usage

```bash
$ python find_module.py <module_name> [<module_name> ...] [--details]
```

---

## Example

```bash
$ python find_module.py sys requests token --details

------------ Module: sys ------------
Module 'sys' is built-in (no file path, human-readable code online)


------------ Module: requests ------------
Module 'requests' is located at:
/opt/anaconda3/lib/python3.12/site-packages/requests/__init__.py

File is a package (directory with __init__.py).


------------ Module: token ------------
Module 'token' is located at:
/opt/anaconda3/lib/python3.12/token.py

File is a pure python module (.py file)

```

---

## Requirements

- Python **3.2** or higher (needed for argparse)

