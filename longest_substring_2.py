import itertools

num = int(input())
string_array= []

def unique_substring(sub):
    unique_array = []
    for a in range(3, len(sub)+1):
        for b in itertools.permutations(sub, a):
            unique = list(set(b))
            if(len(unique) == len(list(b))):
                unique_array.append(b)

    if(len(unique_array) == 0):
        print(-1)
    else:
        print("".join(max(unique_array, key=len)))

for i in range(num):
    string = input()
    string_array.append(string)

for j in string_array:
    unique_substring(j)

