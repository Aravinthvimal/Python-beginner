import itertools

n = int(input())
num_array = []
count = 0

for i in range(n):
    number = int(input())
    num_array.append(number)

des_sum = int(input())

for j in itertools.permutations(num_array, 2):
    if(j[0] + j[1] == des_sum):
        count += 1

print(count//2)