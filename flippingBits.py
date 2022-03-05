n = int(input().strip())

for i in range(n):
    elem = int(input())
    print(0xffffffff & ~elem)