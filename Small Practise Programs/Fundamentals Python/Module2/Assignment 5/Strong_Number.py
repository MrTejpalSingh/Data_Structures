# lex_auth_01269437118923571233

def factorial(number):
    fact = 1
    while (number > 0):
        fact = fact * number
        number = number - 1
    return fact


def find_strong_numbers(num_list):
    strong_num_list = []
    for i in num_list:
        num_str = str(i)
        fact_total = 0
        for j in num_str:
            fact_num = factorial(int(j))
            fact_total = fact_total + fact_num
        if fact_total == i:
            strong_num_list.append(i)
    return strong_num_list


num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)