def gcdnaive(a,b):
    if(b == 0):
        return a
    else:
        return gcdnaive(b,a % b)

a = int(input())
b = int(input())

print(gcdnaive(a, b))
