# TYPE CONVERSION

# 1. Implicit Type Conversion
a = 10  # int
b = 5.5  # float        

result = a + b

print("Implicit Conversion:")
print("Result:", result)
print("Data Type:", type(result))


# 2. Explicit Type Conversion

# Integer to Float
num1 = 10
converted_float = float(num1)
print("\nInteger to Float:", converted_float)

# Float to Integer
num2 = 15.8 
converted_int = int(num2)
print("Float to Integer:", converted_int)

# Integer to String
num3 = 100
converted_string = str(num3)
print("Integer to String:", converted_string)

# String to Integer
num4 = "200"
converted_number = int(num4)
print("String to Integer:", converted_number)

# Integer to Boolean
num5 = 1
converted_bool = bool(num5)
print("Integer to Boolean:", converted_bool)


# 3. Checking Data Types
print("\nChecking Data Types:")
print(type(converted_float))
print(type(converted_int))
print(type(converted_string))
print(type(converted_number))
print(type(converted_bool))
 