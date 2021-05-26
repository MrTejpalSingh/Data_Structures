# lex_auth_0127135811649044481146

def find_nine(nums):
    if 9 in nums[:4]:
        return True
    else:
        return False


nums = [1, 9, 4, 5, 6]
print(find_nine(nums))