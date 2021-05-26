# lex_auth_0127136332814499841204

def sum_of_elements(num_list, number):
    result_sum = 0
    for i in range(0,len(num_list)):
        if i == 0:
            if num_list[i] != number and num_list[i+1] != number:
                result_sum += num_list[i]
        elif i == len(num_list)-1:
            if num_list[i] != number and num_list[i-1] != number:
                result_sum += num_list[i]
        else:
            if num_list[i] != number and num_list[i-1] != number and num_list[i+1] != number:
                result_sum += num_list[i]
    return result_sum


num_list = [7,2,10,20,100,7]
number = 10
print(sum_of_elements(num_list, number))