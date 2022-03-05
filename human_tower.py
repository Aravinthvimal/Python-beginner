#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    if(no_of_people <= 1):
        return 1 * 50
    else:
        total_weight = no_of_people * 50 + human_pyramid(no_of_people - 2)
    
    return total_weight

def find_maximum_people(max_weight):
    no_of_people=0
    for i in range(1, max_weight, 2):
        if(human_pyramid(i) > max_weight):
            no_of_people = i - 2
            break
    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1050)
print(max_people)
