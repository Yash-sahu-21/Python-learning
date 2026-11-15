# Python Lists

## 1. Introduction
- A list is an ordered collection of elements.
- Lists are mutable (can be changed after creation).
- Lists allow duplicate values.
- Lists can store different data types.
- Lists use square brackets `[]`.

## 2. Creating a List
```python
fruits = ["Apple", "Banana", "Mango"]
numbers = [10, 20, 30, 40]
```

## 3. Accessing Elements
```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[-1])
```

## 4. Modifying Elements
```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"
print(fruits)
```

## 5. List Slicing
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

## 6. List Methods

| Method | Description |
|---|---|
| `append()` | Adds an element at the end |
| `insert()` | Adds an element at a specific index |
| `extend()` | Adds multiple elements |
| `remove()` | Removes a specific element |
| `pop()` | Removes an element by index |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `count()` | Counts occurrences |
| `index()` | Returns the index |
| `clear()` | Removes all elements |
| `copy()` | Creates a copy of the list |

## 7. List Operations
```python
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)  # Concatenation
print(a * 2)  # Repetition
print(2 in a) # Membership
```

## 8. Taking List Input
```python
numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)
```

## 9. Sorting a List
```python
numbers = [40, 10, 30, 20]

numbers.sort()                 # Ascending
print(numbers)

numbers.sort(reverse=True)     # Descending
print(numbers)
```

## 10. Important Points
- Lists are mutable.
- Lists support indexing and slicing.
- Lists allow duplicate elements.
- Lists can contain multiple data types.
- Lists can store nested lists.