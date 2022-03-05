num = int(input())
weight_list = []
total = 0

for i in range(num):
    weight = int(input())
    weight_list.append(weight)

threshold = int(input())

for j in weight_list:
    if(j > threshold):
        diff = j - threshold
        price = diff * 2
        total += price
    else:
        total += 1

print(total)
