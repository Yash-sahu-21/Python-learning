# Python Dictionary

A **dictionary** is an ordered (python 3.7+) , mutable collection of key-value pairs.

### Features
- Stores data in key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Mutable (changeable).

### Syntax
```python
student = {"name": "Yash", "age": 18, "marks": 95}
```

### Common Methods
- `get()` – Access values
- `keys()` – Get all keys
- `values()` – Get all values
- `items()` – Get key-value pairs
- `update()` – Update dictionary
- `pop()` – Remove an item
- `clear()` – Remove all items

### Loop
```python
for key, value in student.items():
    print(key, value)
```
