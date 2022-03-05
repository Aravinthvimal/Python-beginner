from typing import Counter


num = int(input())
sock_list = list(map(int, input().split()))
sock_set = set(sock_list)

res = 0

for i in sock_set:
    sock_count = sock_list.count(i)
    res += (sock_count // 2)

print(res)
