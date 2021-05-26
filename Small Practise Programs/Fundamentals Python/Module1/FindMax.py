# lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num = -1
    max_list = []
    if num1 < num2:
        for i in range(num1, num2 + 1):
            temp = i
            sum = 0
            while temp != 0:
                last_digit = temp % 10
                temp = temp // 10
                sum = sum + last_digit
            if sum % 3 == 0:
                if 9 < i < 100:
                    if i % 5 == 0:
                        max_list.append(i)
    else:
        max_num = -1
    if len(max_list) >= 1:
        max_num = max(max_list)
        print(max_list)

    return max_num


# Provide different values for num1 and num2 and test your program.
max_num = find_max(21, 33)
print(max_num)