# Notes on Python JSON

## Introduction
Python's `json` module provides methods for manipulating JSON data. JSON (JavaScript Object Notation) is a lightweight data interchange format.

## Importing the JSON Module
```python
import json
```

## JSON Data Types
The following are the JSON data types and their corresponding Python data types:

| JSON Data Type | Python Data Type |
| --- | --- |
| object | dict |
| array | list |
| string | str |
| number | int or float |
| boolean | bool |
| null | None |

## Parsing JSON Data
The `json.loads()` function is used to parse a JSON string into a Python object.

```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

## Converting Python Objects to JSON
The `json.dumps()` function is used to convert a Python object into a JSON string.

```python
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)  # Output: '{"name": "John", "age": 30, "city": "New York"}'
```

## Reading JSON from a File
The `json.load()` function is used to read JSON data from a file.

```python
with open('data.json') as file:
    data = json.load(file)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

## Writing JSON to a File
The `json.dump()` function is used to write JSON data to a file.

```python
data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)
```


<br>

---
---

<br>


```python
class JsonUpdater:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_json()

    def load_json(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def update_json(self, key, value):
        self.data[key] = value
        self.save_json()

    def save_json(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

# Example usage:
updater = JsonUpdater('data.json')
updater.update_json('name', 'Jane')
updater.update_json('age', 31)
``` 