# lex_auth_0127136357873991681201

def exchange_list(number_list):
    first_half = number_list[:len(number_list)//2]
    second_half = number_list[len(number_list)//2: len(number_list)]
    second_half.reverse()
    number_list = second_half + first_half
    return number_list


number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))