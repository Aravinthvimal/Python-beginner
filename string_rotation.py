word = input().split(",")

def right_rotation(elem):
    wordList = list(elem)

    wordList.insert(0, wordList[-1])
    wordList.pop(-1)

    print("".join(wordList))

def left_rotation(elem):
    for _ in range(2):
        wordList = list(elem)

        wordList.insert(len(wordList), wordList[0])
        wordList.pop(0)

        elem = "".join(wordList)

    print("".join(wordList))

for i in word:
    elem,num = i.strip().split(":")
    
    total = 0

    for j in num:
        total += int(j)**2

    if(total %2 == 0):
        right_rotation(elem)
    else:
        left_rotation(elem)