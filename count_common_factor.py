num1,num2 = map(int, input().split())
count = 0

def factors(num):
    factors_list = []
    for i in range(1, num):
        if(num %i == 0):
            factors_list.append(i)
    
    return factors_list

num1_factors = factors(num1)
num2_factors = factors(num2)

for j in num1_factors:
    if(j in num1_factors and j in num2_factors):
        count += 1

print(count)