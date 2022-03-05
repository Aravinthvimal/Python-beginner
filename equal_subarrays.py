num_list = list(map(int, input().split())) 

for i in range(len(num_list)):
    left = list(num_list[:i])
    right = list(num_list[i+1:])
    if(sum(left) == sum(right)):
        print(i)


print("Hello {O!r} and {O!s}".format('CCC', 'bin'))
