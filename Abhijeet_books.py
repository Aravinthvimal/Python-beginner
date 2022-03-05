n = int(input())
earn_array = list(map(int, input().split()))
cost_array = list(map(int, input().split()))
total = 0

for i,j in zip(earn_array,cost_array):
    total += j - i 

print(total)