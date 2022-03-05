
student_grades = []

for i in range(int(input())):
    name = input()
    score = float(input())
    student_grades.append([name,score])

sorted_grades = sorted(list(set(x[1] for x in student_grades)))
second_last = sorted_grades[1]

student_list = []
for student in student_grades:
    if second_last == student[1]:
        student_list.append(student[0])
            
for student in sorted(student_list):
    print(student)