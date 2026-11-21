# Example solution: sort list of dictionaries
students = [
    {"name": "praveen", "marks": 75},
    {"name": "Rama", "marks": 90},
    {"name": "sita", "marks": 82},
]

by_marks = sorted(students, key=lambda d: d["marks"])
print("By marks ascending:", by_marks)

by_marks_desc = sorted(students, key=lambda d: d["marks"], reverse=True)
print("By marks descending:", by_marks_desc)