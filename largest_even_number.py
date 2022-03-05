from itertools import permutations

word = input()
numList = []
evenList = []

for i in word:
    if(i.isnumeric()):
        numList.append(i)

numList = list(set(numList))
perm = list(permutations(numList))

for i in perm:
    num = int("".join(i))
    if(num %2 == 0):
        evenList.append(num)
    
if(len(evenList) == 0):
    print(-1)
else:
    print(max(evenList))
    