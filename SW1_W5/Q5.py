student_data = [
    {'student_id': '12345', 'grade1': 47, 'grade2': 20, 'grade3': 65},
    {'student_id': '54321', 'grade1': 77, 'grade2': 50, 'grade3': 45},
    {'student_id': '24689', 'grade1': 67, 'grade2': 80, 'grade3': 15}
]

print("Student data report")
print("===================")
for student in student_data:
    average = "%.2f" % round((student['grade3'] + student['grade2'] + student['grade1']) / 3, 2)
    print(
        f"Student id: {student['student_id']}, grade1: {student['grade1']}, grade2: {student['grade2']}, grade3: {student['grade3']}. "
        f"Average for student is: {average}")
