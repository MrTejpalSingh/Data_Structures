#lex_auth_01269442760027340879

def find_smallest_number(num):
    k = 0
    res = num + 1
    while k != num:
        k = 0
        for i in range(1,res+1):
            if res%i == 0:
                k += 1
        res += 1
    return res-1
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)