student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Create an empty dictionary called student_grades.
studentGrades = {}

for student in student_scores:
    #grade = ""
    score = student_scores[student]

    if score > 90:
        studentGrades[student] = "Outstanding"
    elif score > 80:
        studentGrades[student] = "Exceeds Expectations"
    elif score > 70:
        studentGrades[student] = "Acceptable"
    else:
        studentGrades[student] = "Fail"

print(studentGrades)