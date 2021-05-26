#lex_auth_01269446157664256093

def check_prime(number):
    if number == 2:
        return True
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

def rotations(num):
    num_str = str(num)
    lst_of_rot = []
    for i in range(0,len(num_str)):
        sub_lst_of_rot = []
        sub_lst_of_rot.append(num_str[i])
        j = (i+1) % len(num_str)
        while j != i:
            sub_lst_of_rot.append(num_str[j])
            j = (j+1) % len(num_str)
        sub_str_of_rot = "".join(sub_lst_of_rot)
        lst_of_rot.append(int(sub_str_of_rot))
    return lst_of_rot


def get_circular_prime_count(limit):
    lst = []
    for i in range(2,limit+1):
        if check_prime(i) == True:
            # print(i)
            if i < 10:
                lst.append(i)
            else:
                lst_of_rot = rotations(i)
                counter = 0
                for j in lst_of_rot:
                    if check_prime(j) ==True:
                        counter += 1
                if len(str(i)) == counter:
                    lst.append(i)
    return lst


#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
# print(rotations(37))
# print(check_prime())