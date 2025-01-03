# Sphinx Extension: Feature Flags

<!-- Badges go here on the same line; PyPi doesn't support `\` or single-multi-line (it'll stack vertically) -->
[![PyPI](https://img.shields.io/pypi/v/sphinx-feature-flags)](https://pypi.org/project/sphinx-feature-flags/) [![PyPI - License](https://img.shields.io/pypi/l/sphinx-feature-flags)](https://opensource.org/licenses/MIT)

## Description

This Sphinx extension allows for the `feature-flag` directive to show (if `True`) or fallback (if `False` and
using the `:fallback:` option).

## Setup

1. Add the following to your `conf.py`:

    ```python
    import sys, os
    
    sys.path.append(os.path.abspath(os.path.join('_extensions', 'sphinx_feature_flags')))
    extensions = ['sphinx_feature_flags']
    
    feature_flags = {
        'production-stage': False,  # Example
    }
    ```

## Usage

In any `.rst` file, wrap the `feature-flag` directive around any block:

    ```rst
    .. feature-flag:: dev-debug-mode
    
       This only shows if production-stage = True; it can be an entire toctree, too!
    
    .. feature-flag:: dev-debug-mode
       :fallback:
    
       This only shows if production-stage = False.
    ```

## Requirements

- Python>=3.6
- Sphinx>=1.8

This may work with older versions, but has not been tested.

## Entry Point

See `setup(app)` definition at `sphinx_feature_flags.py`.

## Tested in

- Windows 11 via PowerShell 7
- Ubuntu 22.04 via ReadTheDocs (RTD) CI

## Notes

- `__init__.py` is required for both external pathing and to treat the directory as a pkg
