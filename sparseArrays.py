def matchingStrings(strings, queries):

    numArray = []

    for i in queries:
        count = 0
        for j in strings:
            if(i == j):
                count += 1
        numArray.append(count)
    
    return numArray

if __name__ == '__main__':
    
    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    print(matchingStrings(strings, queries))
