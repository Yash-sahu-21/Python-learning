# Python Tuples

## 1. Introduction
- A tuple is an ordered collection of elements.
- Tuples are immutable (cannot be changed after creation).
- Tuples allow duplicate values.
- Tuples can store different data types.

## 2. Creating a Tuple
```python
numbers = (10, 20, 30, 40)
```

## 3. Single Element Tuple
```python
a = (10,)
```
A comma is required for a single-element tuple.

## 4. Accessing Elements
```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[-1])
```

## 5. Tuple Slicing
```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

## 6. Tuple Methods

| Method | Description |
|---|---|
| `count()` | Counts occurrences of an element |
| `index()` | Returns the index of an element |

## 7. Tuple Operations
```python
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)  # Concatenation
print(a * 2)  # Repetition
print(2 in a) # Membership
```

## 8. Tuple Unpacking
```python
student = ("Yash", 18, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)
```

## 9. Important Points
- Tuples are immutable.
- Tuples support indexing and slicing.
- Tuples use round brackets `()`.
- Tuples can contain lists and other tuples.
- Tuples are useful for storing fixed data.