# lex_auth_0127136008767324161169

def close_number(num1, num2, num3):
    num_list = [num1,num2,num3]
    flag = 0
    for i in range(0,len(num_list)):
        j = (i+1) % 3
        while j != i:
            if num_list[i] - num_list[j] == 1 or num_list[i] == num_list[j]:
                flag = 1
                k = (j+1) % 3
                if k == i:
                    k = (i + 1) % 3
                if num_list[k] - num_list[j] >= 2 and num_list[k] - num_list[i] >= 2:
                    return True
                elif num_list[i] - num_list[k] >= 2 and num_list[j] - num_list[k] >= 2:
                    return True
                else:
                    return False
            else:
                j = (j + 1) % 3
    if flag == 0:
        return False
print(close_number(6,6,9))