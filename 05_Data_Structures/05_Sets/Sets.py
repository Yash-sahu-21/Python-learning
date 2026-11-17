
# Python Sets

# 01. Creating a Set
numbers = {10, 20, 30, 40, 50}
print(numbers)
print(type(numbers))


# 02. Duplicate Values
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)


# 03. Adding Elements
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)


# 04. Adding Multiple Elements
numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)


# 05. Removing Elements
numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)

numbers.discard(50)
print(numbers)


# 06. Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))


# 07. Intersection
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))


# 08. Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))


# 09. Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))


# 10. Loop Through a Set
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)


# 11. Check Element
numbers = {10, 20, 30, 40}

if 20 in numbers:
    print("Found")
else:
    print("Not Found")


# 12. Set Length
numbers = {10, 20, 30, 40}
print(len(numbers))


# 13. Clear Set
numbers = {10, 20, 30}
numbers.clear()
print(numbers)


# 14. Remove Duplicates from List
numbers = [10, 20, 20, 30, 30, 40]
unique_numbers = set(numbers)
print(unique_numbers)


# 15. Subset and Superset
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
print(b.issuperset(a))
