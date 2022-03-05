numList = list(map(int, input().split(",")))

total = 0
index_five = numList.index(5)
index_eight = numList.index(8)

for i in numList:
    if(numList.index(i) < index_five or numList.index(i) > index_eight):
        total += i

conc = int("".join([str(i) for i in numList[index_five:index_eight+1]]))

print(conc + total)