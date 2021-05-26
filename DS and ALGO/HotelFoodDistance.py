# lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0

    if quantity_ordered >= 1:
        if distance_in_kms > 0:
            if distance_in_kms > 3:
                dis = 4
                while dis <= distance_in_kms:
                    while dis <= 6 and dis <= distance_in_kms:
                        bill_amount = bill_amount + 3
                        dis += 1
                    if dis <= distance_in_kms:
                        bill_amount = bill_amount + 6
                        dis += 1
            else:
                bill_amount = 0

            if food_type == 'V':
                bill_amount = 120 * quantity_ordered + bill_amount
            elif food_type == 'N':
                bill_amount = 150 * quantity_ordered + bill_amount
            else:
                bill_amount = -1
        else:
            bill_amount = -1
    else:
        bill_amount = -1

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 5)
print(bill_amount)