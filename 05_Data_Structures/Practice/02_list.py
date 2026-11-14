


#  Ascending and Descending Order

# Taking User Input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #  .split() use to separate with space

# Display Original List
print("Original List:", numbers)

# Ascending Order
ascending = sorted(numbers)
print("Ascending Order:", ascending)

# Descending Order
descending = sorted(numbers, reverse=True)
print("Descending Order:", descending)
