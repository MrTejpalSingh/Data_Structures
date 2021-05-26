#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    num_str = str(card_number)
    sum1 = 0
    sum2 = 0
    if len(num_str) == 16:
        for i in range(0,len(num_str)):
            if i%2 == 0:
                if int(num_str[i]) * 2 > 9:
                    dub = str(int(num_str[i]) * 2)
                    print(dub)
                    sum2 = sum2 + (int(dub[0]) + int(dub[1]))
                else:
                    sum2 = sum2 + int(num_str[i]) * 2
            else:
                sum1 = sum1 + int(num_str[i])
    if (sum1 + sum2) % 10 == 0:
        return True
    else:
        return False


card_number = 5239512608615007 #1456734512345698  #4539869650133101
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")