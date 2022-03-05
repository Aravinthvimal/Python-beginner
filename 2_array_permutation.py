num = int(input())

for i in range(num):
    n, k = int(input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    
    list_a.sort()
    list_b.sort(reverse=True)

    for j in range(0, n):
        print(list_a[j] + list_b[j])

