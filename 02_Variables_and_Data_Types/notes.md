# Variables, Data Types and User Input in Python

## 1. Variables
A variable is a name used to store data in a program.

```python
name = "Yash"
age = 18
```
**Rules:**
- Must start with a letter or underscore.
- Cannot start with a number.
- Variable names are case-sensitive.

**Dynamic Typing:** Python allows a variable to store different data types without declaring its type.

## 2. Data Types
Data types define the type of value stored in a variable.

| Data Type | Example |
|---|---|
| int | `10` |
| float | `10.5` |
| str | `"Python"` |
| bool | `True` |
| list | `[1, 2, 3]` |
| tuple | `(1, 2, 3)` |
| set | `{1, 2, 3}` |
| dict | `{"name": "Yash"}` |

**Type Checking:** Use `type()` to check a variable's data type.

```python
x = 10
print(type(x))
```

## 3. Type Conversion
Type conversion means changing one data type into another.

- `int()` – Integer
- `float()` – Float
- `str()` – String
- `bool()` – Boolean

```python
x = "100"
y = int(x)
print(y)
```

## 4. User Input
The `input()` function is used to take input from the user.

```python
name = input("Enter your name: ")
print(name)
```

**Integer Input:**
```python
age = int(input("Enter your age: "))
```

**Float Input:**
```python
marks = float(input("Enter your marks: "))
```

**Important:** The `input()` function always returns a string by default.

