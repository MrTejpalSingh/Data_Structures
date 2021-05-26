
"""
---------------------------------------More Advanced Solution--------------------------------------------------------------------
"""

# # lex_auth_01269441913243238467
#
# def create_largest_number(number_list):
#     num_str = ""
#     for i in number_list:
#         st = str(i)
#         for j in st:
#             num_str = num_str + " " + j
#     single_digit_splited_list = num_str.split(" ")
#     single_digit_splited_list.sort()
#     single_digit_splited_list.reverse()
#     print(single_digit_splited_list)
#     num_str = ""
#     for i in single_digit_splited_list:
#         st = str(i)
#         for j in st:
#             num_str = num_str  + j
#     return int(num_str)
# number_list = [23, 45, 67]
# largest_number = create_largest_number(number_list)
# # print(largest_number)

"""
---------------------------------------Actual Solution--------------------------------------------------------------------
"""

# lex_auth_01269441913243238467

def create_largest_number(number_list):
    number_list.sort()
    number_list.reverse()
    num_str = ""
    for i in number_list:
        st = str(i)
        for j in st:
            num_str = num_str + j
    return int(num_str)


number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)