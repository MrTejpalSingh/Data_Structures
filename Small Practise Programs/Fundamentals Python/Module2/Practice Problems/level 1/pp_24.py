# lex_auth_0127136213490565121191

def find_gcd(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1,small + 1):
        if  num1 % i == 0 and num2 % i == 0:
            last = i
    return last

num1 = 800
num2 = 2800
print(find_gcd(num1, num2))