from asyncio.windows_events import NULL


stocks = list(map(int, input().split())) + [NULL]
print(stocks)
flag = 1

for i in range(len(stocks)-1):
    if(stocks[i] < stocks[i+1] and flag == 1):
        print("Buy stocks on day" , (i+1) , stocks[i] )
        flag = 0
    elif(stocks[i] > stocks[i+1] or i == (len(stocks)-1)):
        print("Sell stocks on day" , (i+1) , stocks[i])
        flag = 1
    elif(stocks[i] < stocks[i+1]):
        continue
    
    

