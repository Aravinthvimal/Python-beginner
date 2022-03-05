m, n = input().split()
numList = []
numList2 = []
m = int(m)
n = int(n)

for i in range(m+n):
    elem = input()
    if(i < m):
        numList.append(elem)
    else:
        numList2.append(elem)

for i in range(1, n):
    for j in range(1, m):
        if(numList[j+1] == numList[i+1]):
            print(j, end=" ")
    print("\n")
