def find_ten_substring(num_str):
    list_of_subs = []
    for i in range(0,len(num_str)):
        sub_str = " "
        sum = int(num_str[i])
        j = i+1
        subs = []
        subs.append(num_str[i])
        while j <= len(num_str) - 1:
            if sum <= 10:
                if sum == 10:
                    # print(sum,num_str[j])
                    if int(num_str[j]) == 0:
                        sub_str = "".join(subs)
                        list_of_subs.append(sub_str)
                        subs.append(num_str[j])
                    break
                else:
                    subs.append(num_str[j])
                    sum = sum + int(num_str[j])
                    j += 1
            else:
                break
        sub_str = "".join(subs)
        list_of_subs.append(sub_str)
    # print(list_of_subs)
    i = 0
    while i < len(list_of_subs):
        flag = 0
        sum = 0
        for j in list_of_subs[i]:
            sum = sum + int(j)
        if sum != 10:
            list_of_subs.remove(list_of_subs[i])
            # print(list_of_subs)
            flag = 1
        if flag == 0:
            i += 1
    # num_str = " ".join(list_of_subs)
    return list_of_subs
num_str = "2825302"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)