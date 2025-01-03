# DictToObject

`DictToObject` is a Python utility class that converts dictionaries into objects, allowing you to access keys as attributes.

## Installation

Install using pip:

```bash
pip install dicttoobject
```

## Dependencies
- termcolor: python

## Example

1. Import the `DictToObject` class:

```python
from dicttoobject import DictToObject
```

2. Create a dictionary:

```python
data = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York'
    }
}
```

3. Convert the dictionary into an object:

```python

obj = DictToObject(data)

# Accessing attributes
print(obj.name)  # Output: John Doe
print(obj.age)  # Output: 30
```

