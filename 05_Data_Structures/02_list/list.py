# LIST 



# 1. Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Fruits:", fruits)

# 2. Accessing List Elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# 3. Updating List Elements
fruits[1] = "Grapes"
print("Updated List:", fruits)

# 4. Adding Elements
fruits.append("Pineapple")
print("After Append:", fruits)

fruits.insert(1, "Cherry")
print("After Insert:", fruits)

# 5. Removing Elements
fruits.remove("Mango")
print("After Remove:", fruits)

fruits.pop()
print("After Pop:", fruits)

# 6. List Length
print("Total Fruits:", len(fruits))

# 7. Sorting a List
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print("Sorted Numbers:", numbers)

# 8. Reversing a List
numbers.reverse()
print("Reversed Numbers:", numbers)

# 9. Looping Through a List
print("All Fruits:")
for fruit in fruits:
    print(fruit)

# 10. Checking an Element
if "Apple" in fruits:
    print("Apple is available")
else:
    print("Apple is not available")

# 11. List Slicing
print("First Two Fruits:", fruits[:2])

# 12. Clearing a List
sample = [1, 2, 3]
sample.clear()
print("Cleared List:", sample)
