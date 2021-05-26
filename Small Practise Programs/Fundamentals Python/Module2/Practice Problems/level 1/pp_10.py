#lex_auth_0127135945621340161163

def string_both_ends(input_string):
    if len(input_string) > 2:
        return input_string[0:2] + input_string[-2:]
    elif len(input_string) < 2:
        return -1
    else:
        return input_string + input_string

input_string="2"
print(string_both_ends(input_string))