# lex_auth_012693825794351104168
"""
----------------------------------------------------First Attempt--------------------------------------
"""
# def find_common_characters(msg1, msg2):
#     common_characters = ""
#     flag = 0
#     for i in msg1:
#         for j in msg2:
#             if i == j:
#                 if i != " ":
#                     common_characters = common_characters + i
#                     flag = 1
#                     break
#     if flag == 0:
#         return -1
#     return common_characters

"""x
---------------------------------------------------Second Attempt--------------------------------------
"""

def find_common_characters(msg1, msg2):
    str_char = ""
    for i in msg1:
        for j in msg2:
            if i == j:
                if j not in str_char:
                    str_char = str_char + j
    if len(str_char) > 0:
        return str_char
    else:
        return -1

# Provide different values for msg1,msg2 and test your program
msg1 = "Moto"
msg2 = "Apple"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)