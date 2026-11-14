
# Tuples 

# 1. Creating a Tuple
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Fruits:", fruits)

# 2. Accessing Tuple Elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# 3. Tuple with Different Data Types
student = ("Yash", 18, 85.5, True)
print("Student Details:", student)

# 4. Tuple Length
print("Total Elements:", len(fruits))

# 5. Tuple Slicing
print("First Two Fruits:", fruits[:2])

# 6. Looping Through a Tuple
print("All Fruits:")
for fruit in fruits:
    print(fruit)

# 7. Checking an Element
if "Apple" in fruits:
    print("Apple is available")

# 8. Counting Elements
numbers = (10, 20, 10, 30, 10, 40)
print("Count of 10:", numbers.count(10))

# 9. Finding Index
print("Index of Mango:", fruits.index("Mango"))

# 10. Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined Tuple:", combined)

# 11. Tuple Repetition
repeated = tuple1 * 2
print("Repeated Tuple:", repeated)

# 12. Tuple Unpacking
name, age, marks = ("Yash", 18, 90)
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# 13. Converting List into Tuple
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print("Converted Tuple:", my_tuple)

# 14. Converting Tuple into List
new_list = list(fruits)
print("Converted List:", new_list)

# 15. Single Element Tuple
single = (10,)
print("Single Element Tuple:", single)
