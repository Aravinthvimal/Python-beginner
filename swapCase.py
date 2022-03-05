def swap_case(s):

    Output = ''
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower())
        elif(char.islower()==True):
            Output += (char.upper())
        else:
            Output += char
    return Output


print(swap_case('HackerRank.com presents "Pythonist 2".'))


