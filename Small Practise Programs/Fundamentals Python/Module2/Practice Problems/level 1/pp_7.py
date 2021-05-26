# lex_auth_0127135857243832321154

def seed_no(number, ref_no):
    str_num = str(number)
    mul = number
    for i in str_num:
        mul = mul * int(i)
    if mul == ref_no:
        return True
    else:
        return False
number = 123
ref_no = 738
print(seed_no(number, ref_no))