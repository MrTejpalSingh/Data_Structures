# lex_auth_0127135838317445121147

def count_digits_letters(sentence):
    str_num = "1234567890"
    digits = 0
    chars = 0
    for i in sentence:
        if i in str_num:
            digits += 1
        elif "a" <= i <= "z" or "A" <= i <= "Z":
            chars += 1
    result_list = []
    result_list.append(chars)
    result_list.append(digits)
    return result_list


sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))