# strings

# CREATEING A STRING
name = "Yash Sahu"
print(name)

# STRING LENGTH
print(len(name))

# ACCESSING CHARACTERS IN A STRING
print(name[0])  # First character
print(name[1])  # Second character
print(name[2])  # Third character
print(name[3])  # Fourth character

# STRING SLICING
print(name[0:3])  # First three characters

# *****STRING METHODS*****

# UPPERCASE
print(name.upper())

# LOWERCASE
print(name.lower())

# REPLACE
print(name.replace("a", "o"))

# CAPITALIZE
print(name.capitalize())

# TITLE 
print(name.title())

# REMOVE WHITESPACE
name_with_whitespace = "   Yash   "
print(name_with_whitespace.strip())

# CHECK IF STRING STARTS WITH A SPECIFIC CHARACTER
print(name.startswith("Y")) 

# CHECK IF STRING ENDS WITH A SPECIFIC CHARACTER
print(name.endswith("u"))

# FINDING A SUBSTRING
print(name.find("Sahu"))  # Returns the starting index of the substring

# CHECKING A WORD IN A STRING
print("Sahu" in name)  # Returns True if "Sahu" is found

# STRING CONCATENATION
full_name = name + " is a student."
print(full_name)

# STRING FORMATTING
age = 19
print(f"{name} is {age} years old.")

#SPLITTING A STRING
print(name.split(" "))  # Splits the string into a list of words

# COUNTING OCCURRENCES OF A CHARACTER
print(name.count("a"))  # Counts how many times "a" appears in the string

#FINDING CHARACTER INDEX
print(name.index("S"))  # Returns the index of the first occurrence of "S"

# CHECKING IF STRING IS ALPHABETIC,DIGIT OR NUMBER
print(name.isalpha())  # Returns True if all characters are alphabetic
print (name.isdigit())
print (name.isalnum())

# REVERSING A STRING

print (name[::-1])

