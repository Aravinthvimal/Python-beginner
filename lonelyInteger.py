def lonelyinteger(a):
    
    numSet = set(a)

    for i in numSet:
        count = 0
        for j in a:
            if(i == j):
                count += 1
        if(count == 1):
            return i


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))

