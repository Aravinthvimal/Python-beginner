def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    account_number = str(account_number)
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    if(len(account_number) == 4 and account_number[0] == 1):
        print("Account number:", account_number)
        if(account_balance >= 100000):
            if(loan_type == "Car"):
                if(salary >= 25000):
                    if(loan_amount_expected <= 500000):
                        if(customer_emi_expected <= 36):
                            print("The customer can avail the amount of Rs.", eligible_loan_amount)
                            print("Eligible EMIs :", bank_emi_expected)
                            print("Requested loan amount:", loan_amount_expected)
                            print("Requested EMI's:",customer_emi_expected)
                else:
                    ("Invalid loan type or salary")

calculate_loan(1001,40000,250000,"Car",300000,30)