# lex_auth_01269441810970214471

def check_double(number):
    str_num = str(number)
    double_num_str = str(number * 2)
    if len(str_num) == len(double_num_str):
        counter = 0
        for i in str_num:
            if i in double_num_str:
                counter += 1
        if counter == len(str_num):
            return True
        else:
            return False
    else:
        return False


# Provide different values for number and test your program
print(check_double(125874))