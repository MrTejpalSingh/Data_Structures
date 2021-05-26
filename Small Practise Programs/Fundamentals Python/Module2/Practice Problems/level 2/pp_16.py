# lex_auth_0127136084107673601177

def rotate_list(input_list, n):
    second_half = input_list[-n:]
    first_half = input_list[:-n]
    output_list = second_half + first_half

    return output_list


input_list = [1, 2, 3, 4, 5, 6]
output_list = rotate_list(input_list, 4)
print(output_list)