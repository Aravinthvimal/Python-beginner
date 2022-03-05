num = int(input())
price_list = []
product_list = []

for i in range(num):
    item = list(input().split())
    price_list.append(item[-1])
    product_list.append(" ".join(item[:-1]))

checked = []

for j in product_list:
    if(j not in checked):
        quantity = product_list.count(j)
        index = product_list.index(j)
        price = price_list[index]
        print(j, quantity * int(price))
        checked.append(j)



