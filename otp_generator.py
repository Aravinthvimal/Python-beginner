import itertools

perm_list = []
inp = input()

for i in range(3, len(inp)):
    for j in itertools.permutations(inp, i):
        word = "".join(j).lower()
        length = len(j)
        char_length = len(set(j))
        if(length == char_length):
            perm_list.append("".join(j))
    
print(max(perm_list, key=len))


