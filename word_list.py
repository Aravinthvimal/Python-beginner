import itertools
numArray = []
resArray = []
count = 0

num1 = int(input())
num2 = int(input())

for i in range(num1, num2+1):
    numArray.append(i)

print(numArray)

n = len(numArray)
indices = list(range(n+1))
for i,j in itertools.combinations(indices,2):
    resArray.append((numArray[i:j]))

print(resArray)

for k in resArray:
    if(len(k) %2 != 0):
        count += 1
    
print(count)