def temp_conversion(temp):
    celsius = (temp - 32) * (5 / 9)
    farenheit = temp/(5/9) + 32
    print(celsius, farenheit)
    
    
temp = 32
temp_conversion(temp)
