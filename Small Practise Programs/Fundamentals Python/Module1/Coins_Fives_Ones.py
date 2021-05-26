#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed = 0
    one_needed = 0

    if no_of_five * 5 >= rupees_to_make:
        if no_of_five * 5 == rupees_to_make:
            five_needed = no_of_five
            one_needed = 0
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            if rupees_to_make % 5 == 0:
                five_needed = rupees_to_make // 5
                one_needed = 0
                print("No. of Five needed :", five_needed)
                print("No. of One needed  :", one_needed)
            else:
                five_needed = rupees_to_make // 5
                one_needed = rupees_to_make - five_needed * 5
                if no_of_one >= one_needed:
                    print("No. of Five needed :", five_needed)
                    print("No. of One needed  :", one_needed)
                else:
                    print(-1)
    else:
        five_needed = no_of_five
        one_needed = rupees_to_make - five_needed * 5
        if no_of_one >= one_needed:
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(100,21,5)