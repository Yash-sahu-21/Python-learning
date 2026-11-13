# GRADE_CHECKER.PY


percentage = float(input("Enter your percentage (0-100): "))

if percentage >= 95:
    print("Grade A+")
elif percentage >= 90:
    print("Grade A")
elif percentage >= 85:
    print("Grade A-")
elif percentage >= 80:
    print("Grade B+")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 70:
    print("Grade B-")
elif percentage >= 65:
    print("Grade C+")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 55:
    print("Grade C-")
elif percentage >= 50:
    print("Grade D+")
elif percentage >= 45:
    print("Grade D")
elif percentage >= 36:
    print("Grade D-")
elif percentage >= 0:
    print("Fail")
else:
    print("Invalid Percentage")