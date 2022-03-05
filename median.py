n = int(input())
numList = list(map(int, input().split()))
numList.sort()
med = n // 2

print(numList[med])