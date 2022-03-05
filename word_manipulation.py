num = list(input())
num_list = []
pronic = []

def pronic_number(n):
    for k in range(0, (n // 2)+1):
        if(k * (k+1) == n):
            return True

for i in range(len(num)):
    for j in range(i, (len(num))):
        number = "".join(num[i:j])
        if(len(number) > 0 and str(number) not in num_list):
            num_list.append(number)

for b in num_list:
    if(pronic_number(int(b))):
        pronic.append(int(b))
    
pronic.sort()
print("".join(pronic))