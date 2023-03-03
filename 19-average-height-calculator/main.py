student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

totalHeights = 0
totalStudent = 0
for heights in student_heights:
    totalHeights += heights
    totalStudent += 1

average = round(totalHeights / totalStudent)
print(average)


