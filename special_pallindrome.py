listSample=list(input())
 
i=0
j=len(listSample)-1
 
while i<j:
    if not listSample[i].isalpha():  #checks the strt of the string is a spzl char
        i += 1
    elif not listSample[j].isalpha():  #checks the end of the string is a spzl char
        j -= 1
    else:
        listSample[i], listSample[j]=listSample[j], listSample[i] #if both are NOT spzl char swap them
        i+=1
        j-=1

strOut=''.join(listSample)
print(strOut)