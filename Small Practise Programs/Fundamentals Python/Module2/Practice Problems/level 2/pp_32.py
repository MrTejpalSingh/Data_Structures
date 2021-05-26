#lex_auth_0127136357122129921205

def check_squares(number):
    for i in range(1,number):
        for j in range(1,i):
            if i*i + j*j == number:
                # print(i,j)
                return True
    return False



number=13
print(check_squares(number))