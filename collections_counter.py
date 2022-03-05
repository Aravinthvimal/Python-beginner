list_len = int(input())
shoe_size_list = list(map(int, input().split()))
costomer_len = int(input())
costomer_list = []
total = 0

for i in range(costomer_len):
    cos, price = input().split()
    costomer_list.extend((int(cos), int(price)))

for i in range(len(costomer_list)):
    if(costomer_list[i] in shoe_size_list):
        total += costomer_list[i+1]
        shoe_size_list.remove(costomer_list[i])

print(total)
