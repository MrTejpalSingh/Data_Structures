# lex_auth_0127135739583692801137

def add_string(str1):
    if len(str1) >= 3:
        if str1[-3:] == "ing":
            str1 = str1 + "ly"
        else:
            str1 = str1 + "ing"

    return str1


str1 = "coming"
print(add_string(str1))