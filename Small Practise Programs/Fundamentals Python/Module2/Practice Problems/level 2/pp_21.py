# lex_auth_0127136209566679041189

def check_numbers(num1, num2):
    num_list = set()
    count = 0
    for i in range(num1 + 1, num2+1):
        for j in range(num1, i):
            if i % j  == 0:
                num_list.add(i)
                count += 1
                break


    return [num_list, count]


num1 = 2
num2 = 20
print(check_numbers(num1, num2))