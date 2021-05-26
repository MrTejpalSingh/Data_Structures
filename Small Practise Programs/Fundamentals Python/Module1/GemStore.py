# lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0
    counter = 0
    for rg in range(0,len(reqd_gems)):
        for lg in range(0,len(gems_list)):
            if reqd_gems[rg] == gems_list[lg]:
                bill_amount = bill_amount + reqd_quantity[rg] * price_list[lg]
                counter += 1
    if counter != len(reqd_gems):
        bill_amount = -1
    else:
        if bill_amount > 30000:
            discount = (5 * bill_amount) / 100
            bill_amount = bill_amount - discount
    return bill_amount


# List of gems available in the store
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]

# Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list = [1760, 2119, 1599, 3920, 3999]

# List of gems required by the customer
reqd_gems = ["Ivory", "Emerald", "Garnet"]

# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity = [3, 10, 12]

bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)