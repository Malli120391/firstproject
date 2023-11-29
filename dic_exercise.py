student_marks={
    "AB":92,
    "CD":78,
    "EF":56,
    "GH":41,
    "IJ":99,
    "KL":34
}
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        marks=student_grades[student]="A+"
    elif marks > 80:
        marks = student_grades[student] = "A"
    elif marks > 70:
        marks = student_grades[student] = "B+"
    elif marks > 60:
        marks = student_grades[student] = "B"
    elif marks > 50:
        marks = student_grades[student]="C+"
    elif marks > 40:
        marks = student_grades[student]="D"
    else:
        student_grades[student]="F"
print(student_grades)

