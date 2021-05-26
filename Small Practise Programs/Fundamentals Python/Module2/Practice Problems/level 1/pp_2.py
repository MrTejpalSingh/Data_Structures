# lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    if input_str[0] == ")" or input_str[-1] == "(":
        return False
    else:
        if input_str.count("(") == input_str.count(")"):
            return True
        else:
            return False

input_str = "(())("
print(bracket_pattern(input_str))