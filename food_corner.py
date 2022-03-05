def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0

    if((food_type == "N" or food_type == "V") and quantity_ordered >= 1 and distance_in_kms > 0):

        if(food_type == "V"):
            food_bill = 120 * quantity_ordered
        elif(food_type == "N"):
            food_bill = 150 * quantity_ordered

        if(distance_in_kms <= 3):
            distance_bill = 0
        elif(distance_in_kms > 3 and distance_in_kms <= 6):
            distance_in_kms = distance_in_kms - 3
            distance_bill = distance_in_kms * 3
        elif(distance_in_kms > 6):
            distance_bill = 9
            distance_in_kms = distance_in_kms - 6
            distance_bill += distance_in_kms * 6

        bill_amount = food_bill + distance_bill
    
    else:
        bill_amount = -1
    
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)