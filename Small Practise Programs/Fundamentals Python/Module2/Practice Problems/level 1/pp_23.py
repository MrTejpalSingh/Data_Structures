# lex_auth_0127136251125350401190

def divisible_by_sum(number):
    sum = 0
    str_num = str(number)
    for i in str_num:
        sum = sum + int(i)
    if number % sum == 0:
        return True
    else:
        return False


number = 42
print(divisible_by_sum(number))