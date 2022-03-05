num = int(input())
people_list = []
house_list = []
count = 0

for i in range(num*2):
    if(i < num):
        people = int(input())
        people_list.append(people)
    else:
        house = int(input())
        house_list.append(house)

for a in range(len(people_list)):
    for b in range(len(house_list)):
        if(people_list[a] <= house_list[b]):
            house_list[b] = -1
            count += 1
            break

print(num - count)
