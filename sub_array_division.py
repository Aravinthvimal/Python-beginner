len = int(input())
s = list(map(int, input().split()))
dm = input().split()

d = int(dm[0])
m = int(dm[1])

count = 0

for i in range(len(s) - m + 1):
    res = (sum(s[i:m+i]))
    if(res == d):
        count += 1

print(count)
