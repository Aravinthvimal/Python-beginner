
student_grades = []

for i in range(int(input())):
    data = list(input().split(" "))
    name = data[0]
    scores = data[1:]
    student_grades.append(list([name,scores]))

target_name = input()

for student in student_grades:
    if target_name == student[0]:
        total = 0
        avg = 0
        for i in student[1]:
            total = total + float(i)
        
        avg = total/len(student[1])

print("{:.2f}".format(avg))



