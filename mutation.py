def mutate_string(string, position, character):

    res_list = []

    for i in string:
        res_list.append(i)

    res_list[position] = character

    return "".join(res_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)