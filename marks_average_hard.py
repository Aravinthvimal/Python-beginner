num, headers, total = int(input()), list(input().split()), 0
for i in range(num):
    total += int(list(input().split())[headers.index("MARKS")])
print(total/num)