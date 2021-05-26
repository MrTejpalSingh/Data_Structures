# lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    lower = 0
    upper = 0
    for i in sentence:
        if "a" <= i <= "z":
            lower += 1
        elif "A" <= i <= "Z":
            upper += 1
    result_list = []
    result_list.append(upper)
    result_list.append(lower)
    return result_list


sentence = "Come Here"
print(find_upper_and_lower(sentence))