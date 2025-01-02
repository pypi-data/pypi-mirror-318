"""
JSONPath-NZ
===========

A Python library for bidirectional conversion between JSON objects and JSONPath expressions.
Handles complex filter conditions, nested arrays, and maintains data structure integrity.

Author: Yakub Mohammad (yakub@arusatech.com)
Version: 0.1.0
License: MIT
Copyright (c) 2024 Yakub Mohammad / AR USA LLC
"""

from .parse_dict import parse_dict
from .parse_jsonpath import parse_jsonpath

__version__ = "0.1.1"
__author__ = "Yakub Mohammad"
__license__ = "MIT"

__all__ = [
    "parse_dict",
    "parse_jsonpath",
]
