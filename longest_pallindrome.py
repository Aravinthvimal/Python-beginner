import itertools

word = input()
pall_list = []

for i in range(1, len(word)+1):
    for j in itertools.permutations(word, i):
        a = ("".join(j))
        if(a[::-1] == a):
            pall_list.append(a)
    
pall_list.sort(reverse=True, key=len)
print(pall_list[0])