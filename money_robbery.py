amount = int(input())

state = 0

for i in range(0,amount):
    for j in range(0,10):
        if(i + j == amount):
            print(str(i) + str(j))
            state = 1
            break
    if(state == 1):
        break
    

