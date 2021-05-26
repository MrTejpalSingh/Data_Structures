# lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    if distance_in_kms > 0:
        if distance_in_kms >= 4:
            counter = 4
            while counter <= distance_in_kms:
                while counter <= 6 and counter <= distance_in_kms:
                    bill_amount = bill_amount + 3
                    counter += 1
                if counter <= distance_in_kms:
                    bill_amount = bill_amount + 6
                    counter += 1
        else:
            pass
        if quantity_ordered >= 1:
            if food_type == "N":
                bill_amount = quantity_ordered * 150 + bill_amount
            elif food_type == "V":
                bill_amount = quantity_ordered * 120 + bill_amount
            else:
                bill_amount = -1
        else:
            bill_amount = -1
    else:
        bill_amount = -1

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)

"""
Can 

"""