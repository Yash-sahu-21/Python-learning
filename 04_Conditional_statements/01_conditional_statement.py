# Python Conditional Statements

# 1. if Statement
age = 20

if age >= 18:
    print("Adult")


# 2. if-else Statement
number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 3. if-elif-else Statement
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


# 4. Nested if Statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Entry Not Allowed")