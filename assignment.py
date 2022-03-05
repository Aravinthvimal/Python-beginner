#lex_auth_01269437118923571233

def factorial(number):

    total = 0

    for i in str(number):
        total += factorial(int(i))
        print(total)
        
    return total

def find_strong_numbers(num_list):

    strong_num_list = []
    
    for i in num_list:
        if(factorial(i) == i):
            strong_num_list.append(i)
    
    return strong_num_list


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)