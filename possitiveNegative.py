def plusMinus(arr):

    poss_count = 0
    neg_count = 0
    zero_count = 0
    
    for i in arr:
        if(i > 0):
            poss_count += 1

        elif(i < 0):
            neg_count += 1
        
        else: 
            zero_count += 1

    print("{:.6f}".format(poss_count / len(arr)))
    print("{:.6f}".format(neg_count / len(arr)))
    print("{:.6f}".format(zero_count / len(arr)))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
