import itertools

num_array = list(map(int, input().split()))
special_array = []
perm = []

for i in range(3, len(num_array)+1):
    for j in itertools.permutations(num_array, i):
        if(list(j) == sorted(list(j))):
            perm.append(list(j))

for a in perm:
    count = 0
    for b in range(len(a) - 2):
        if(a[b] + a[b+1] == a[b+2]):
            count += 1
        if(count == (len(a) - 2)):
            special_array.append(a)

print(max(special_array, key=len))
