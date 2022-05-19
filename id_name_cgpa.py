num = int(input())
database = []
roll_no = []
name = []
cgpa = []

for i in range(num):
    dataset = list(input().split())
    database.append(dataset)

for j in range(num):
    roll_no.append(database[j][0])
    name.append(database[j][1])
    cgpa.append(database[j][2])

database.sort(key=lambda x: x[2], reverse=True)

for i in range(num):
    if(cgpa.count(database[i][2]) == 1):
        print(database[i][1])
    elif(not(database[i][2] == database[i+1][2])):
        max = i if database[i][2] < database[i+1][2] else (i + 1)
        print(database[max][1])
    else:
        max = i if database[i][0] < database[i+1][0] else (i + 1)
        print(database[max][1])

