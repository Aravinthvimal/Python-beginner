emp_list = list(map(str, input().split(",")))
name = []
number = []

for i in emp_list:
    emp,num = i.strip().split(":")
    name.append(emp)
    num = "".join(list(sorted(num, reverse=True)))
    number.append(num)

for index,elem in enumerate(name):
    length = len(elem)
    if(str(length) in number[index]):
        print(elem[-1], end="")
    elif True:
        for i in range(len(number[index])):
            count = 0
            if(int(number[index][i]) < length):
                print(elem[int(number[index][i])-1], end="")
                count += 1
                break
        if(count == 0):
            print("X", end="")
            break
