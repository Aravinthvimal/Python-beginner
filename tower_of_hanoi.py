def towerOfHanoi(n, source, destination, auxiliary):
    if(n == 0):
        print("Move disc 1 from source", source, "to destination", destination)
        return
    
    towerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disc", n, "from source", source, "to destination", destination)
    towerOfHanoi(n-1, auxiliary, destination, source)

n = int(input()) # enter input 4

towerOfHanoi(n, "A", "B", "C")