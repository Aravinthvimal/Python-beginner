import math


num = int(input())
num_array = []
res = 0

def special_number(n):
    numerator = 10
    for k in range(1, n):
        numerator *= (10+k)
    
    denominator = math.factorial(n)
    return numerator/denominator

for i in range(num):
    num = int(input())
    num_array.append(num)

for j in num_array:
    res += special_number(j)

print(int(res))
