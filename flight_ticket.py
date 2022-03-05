def discount_price(adult, children):
    
    total = (adult * 37550) + (children * 37550/3) 

    service_tax = total * 7/100
    total = total + service_tax
    holiday = total * 10/100
    total = total - holiday

    print(total)

discount_price(5,2)
