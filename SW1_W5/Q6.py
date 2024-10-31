import csv

# A
# fields = []
# rows = []
#
# with open('students.csv') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fields = next(csvreader)
#     for row in csvreader:
#         row = row[0].split(';')
#         rows.append(row)
#
# print("Student data report")
# print("===================")
# for student in rows:
#     print(f"Name: {student[0]}")
#     print(f"Grade 1: {student[1]}")
#     print(f"Grade 2: {student[2]}")
#     print(f"Grade 3: {student[3]}")
#     avg = "%.2f" % round((int(student[1]) + int(student[2]) + int(student[3])) / 3, 2)
#     print(f"Average grade for {student[0]}: {avg}")

# B

with open('students.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    students_list = []
    for row in reader:
        row = row[0].split(';')
        student_dict = {
            "name": row[0],
            "grade 1": int(row[1]),
            "grade 2": int(row[2]),
            "grade 3": int(row[3]),
            "grade 4": int(row[4]),
            "grade 5": int(row[5]),
            "grade 6": int(row[6]),
            "grade 7": int(row[7])
        }
        students_list.append(student_dict)

    print(students_list)