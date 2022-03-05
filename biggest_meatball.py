length = int(input())
size = int(input())
meatball_list = list(map(int, input().split()))
res_list = []

while(len(meatball_list) != 0):
    if(meatball_list[0] > size):
        meatball_list[0] = meatball_list[0] - size
        meatball_list.insert(len(meatball_list), meatball_list[0])
        meatball_list.pop(0)
    else:
        meatball_list.pop(0)
    
    res_list.append(meatball_list)

print(len(res_list)//length)


