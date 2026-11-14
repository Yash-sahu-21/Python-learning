

# Student Record Management System

list_of_stu = [(1001,"YASH_SAHU",95),
               (1002,"VISHNU_SHUKLA",90),
               (1003,"VINAYAK_BAKSHI",85),
               (1004,"ARIHANT_JAIN",80)]

# Display Student Records
print("**STUDENT RECORDS**")


for student in list_of_stu:
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
    print("----------------")

# Calculate Average Marks
total = sum(student[2] for student in list_of_stu)
average = total / len(list_of_stu)

print("Average class Marks:", average)
print ("----------------")

# Find Highest Scorer
topper = max(list_of_stu, key=lambda student: student[2])

print("Topper:", topper[1])
print("Highest Marks:", topper[2])
print ("----------------")