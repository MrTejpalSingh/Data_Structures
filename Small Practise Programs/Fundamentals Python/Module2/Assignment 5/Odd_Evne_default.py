#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum = 0
    if filter_func == None:
        for i in list_of_num:
            sum += i
        return sum
    else:
        list_of_elements = filter_func(list_of_num)
        for i in list_of_elements:
            sum += i
            # print(i, sum)
        return sum

def even(data):
    even_nums = []
    for i in data:
        if i%2 == 0:
            even_nums.append(i)
    return even_nums
def odd(data):
    odd_nums = []
    for i in data:
        if i%2 != 0:
            odd_nums.append(i)
    # print(odd_nums)
    return odd_nums

sample_data = range(10,26)

print(sum_of_numbers(sample_data,even))