num = int(input())

def pallindrome(num):
    while True:
        pal = str(num)[::-1]
        s = int(num) + int(pal)
        num = str(s)

        if(str(num) == str(num)[::-1]):
            print(num)
            break

pallindrome(num)
