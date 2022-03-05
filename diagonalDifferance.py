def diagonalDifference(arr):
    
    j = 0
    k = len(arr)-1
    sum = 0
    diff = 0

    for i in range(0, len(arr)):
        sum += (arr[i][j])
        j += 1

        diff += (arr[i][k])
        k -= 1

    return (abs(sum - diff))

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))
