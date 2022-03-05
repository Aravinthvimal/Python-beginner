def countingSort(arr):

    freq = [0]*100

    for i in arr:
        freq[i] = freq[i]+1

    return freq

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(countingSort(arr))