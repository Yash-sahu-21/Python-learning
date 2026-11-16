
# Dictionaries in Python

# 1. Creating a Dictionary
student = {
    "name": "Yash",
    "age": 19,
    "course": "B.Tech CSE",
    "marks": 95
}

print("Student:", student)

# 2. Accessing Values
print("Name:", student["name"])
print("Age:", student.get("age"))

# 3. Adding New Elements
student["city"] = "Jabalpur"
print("After Adding:", student)

# 4. Updating Values
student["marks"] = 98
print("After Updating:", student)

# 5. Removing Elements
student.pop("city")
print("After Pop:", student)

# 6. Dictionary Keys
print("Keys:", student.keys())

# 7. Dictionary Values
print("Values:", student.values())

# 8. Key-Value Pairs
print("Items:", student.items())

# 9. Checking a Key
print("name" in student)

# 10. Dictionary Length
print("Total Items:", len(student))

# 11. Loop Through Dictionary
for key, value in student.items():
    print(key, ":", value)

# 12. Updating Dictionary
student.update({"age": 19, "marks": 99})
print("Updated Dictionary:", student)

# 13. Copy Dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# 14. Clear Dictionary
sample = {"a": 1, "b": 2}
sample.clear()
print("Cleared Dictionary:", sample)
