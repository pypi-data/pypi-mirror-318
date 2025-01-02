# JSONPath-NZ (NextZen)

A Python library for bidirectional conversion between JSON objects and JSONPath expressions, with support for complex filter conditions and array handling.
- `Author` : Yakub Mohammad (yakub@arusatech.com , arusatechnology@gmail.com)
- `Organization` : AR USA LLC
- `License` : MIT

## Features

- Two-way conversion between JSON and JSONPath expressions:
  - Convert JSONPath expressions to JSON objects (`parse_jsonpath`)
  - Convert JSON objects to JSONPath expressions (`parse_dict`)
- Support for complex filter conditions using `extend` parameter
- Handle nested objects and arrays
- Support array indexing and empty objects
- Maintain data structure integrity

## Installation

```bash
pip install jsonpath-nz
```

## Usage

### Converting JSONPath to Dictionary (`parse_jsonpath`)

See the [tests/local_test.py](tests/local_test.py) file for examples.

Define extend parameter for filter conditions


## API Reference

### parse_jsonpath(manifest, extend=None)

Converts JSONPath expressions to a dictionary structure.

Parameters:
- `manifest` (dict): Dictionary with JSONPath expressions as keys and values
- `extend` (dict, optional): Dictionary specifying filter conditions for arrays

Returns:
- dict: Processed dictionary structure



### parse_dict(data, parent_path='$', paths=None, extend=None)

Converts a dictionary to JSONPath expressions.

Parameters:
- `data` (dict): Input dictionary to convert
- `parent_path` (str, optional): Base JSONPath. Defaults to '$'
- `paths` (dict, optional): Dictionary to store results
- `extend` (dict, optional): Dictionary specifying filter fields for arrays

Returns:
- dict: Dictionary with JSONPath expressions as keys and values


## Error Handling

Both functions include error handling for:
- Invalid JSONPath syntax
- Unbalanced brackets or quotes
- Missing required fields
- Invalid filter conditions

Example:

```python
from jsonpath_nz import parse_jsonpath
JSONPath expressions
jsonpath_data = {
    "$.store.book[1].author": "Yakub Mohammad",
    "$.store.local": "False",
    "$.channel": "online",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'Doe')].contact": "9876543210"
}
extend = {
    "borrower": ["firstName", "lastName"]
}
result = parse_jsonpath(jsonpath_data, extend=extend)
print(result)
```

### Converting Dictionary to JSONPath (`parse_dict`)

See  the [tests/local_test.py](tests/local_test.py) file for examples.

```python
from jsonpath_nz import parse_dict

# Dictionary to convert
dict_data = {
    "store": {"book": [{"author": "Yakub Mohammad"}, {"category": "Fiction"}]},
    "channel": "online",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'Doe')].contact": "9876543210"
}

extend = {
    "borrower": ["firstName", "lastName"]
}

result = parse_dict(dict_data, extend=None)
print(result)
```
