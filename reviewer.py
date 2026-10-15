 age = int(input(input age >>>))
monthly_revenue = float(input("how much is you mothly revenue >>>>"))
credit_score = int(input("your credit score >>>"))
yrs_in_business = float("input( years in business >>"))
has_defaults = bool(input( "has default" (True/False) >>))
collateral_name = input("collateral name")
collateral_value = float(input("collateral value >>>"))

max_loan = 0
base_fee = 0

if age >= 21 and yrs >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    if credit_score is >= 720:
        max_loan = rev * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO" ,max_loan)
        print("You have high credit score")
        if monthly_revenue >= 50000:
            print("Revenue higher than 50k")
            base_fee = max_loan * 0.015
            print("Base fee rate is set to", base_fee)
        else:
            print("Revenue lower than 50k")
            base_fee = max_loan * 0.025
            print("Base fee rate is set to", base_fee)
        if collateral_value >= max_loan:
            print("Collateral", collateral, "with a value of", collateral_value, "is Accepted")
        else:
            print("Rejected: Insufficient collateral value for",collateral)

        surge_fee_rate = max_loan * base_fee
        if max_loan % 500 != 0:
            print("Additional Charge Added")
            surge_fee_rate += 250
            print("Updated base fee is",base_fee)
            
    elif credit_score >= 620 and credit_score < 720:
        print("Credit score within range of 620 to 720")
        max_loan = monthly_revenue * 1.5
        print("Maximum loan for this credit score is",max_loan)
        if yrs_in_business >= 5:
            print("Year in business is more than 5")
            base_fee = max_loan * 0.02
            print("base fee rate is set to", base_fee)
        else:
            print("business year is less than 5 yrs")
            base_fee = max_loan * 0.035
            print("Base fee rate is set to", base_fee)
    elif credit_score < 620 and credit_score >= 1:
        print("Credit score is too low")

    else:
        print("INVALID")
else:
    print("BASELINE FAILED")