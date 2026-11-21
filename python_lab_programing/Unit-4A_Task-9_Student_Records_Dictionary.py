# Example solution: student records dictionary
name = "prasanna"
marks = 96

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

student = {"name": name, "marks": marks, "grade": grade}
print("Record:", student)
for key, value in student.items():
    print(f"{key}: {value}")