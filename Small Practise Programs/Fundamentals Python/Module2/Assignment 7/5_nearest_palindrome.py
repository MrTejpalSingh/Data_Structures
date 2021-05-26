"""
There should actually be a constant-time (well it is linear on the number of digits of the input) way to find the next largest palindrome. I will give an algorithm that assumes the number is an even number of digits long (but can be extended to an odd number of digits).

Find the decimal representation of the input number ("2133").
Split it into the left half and right half ("21", "33");
Compare the last digit in the left half and the first digit in the right half.
a. If the right is greater than the left, increment the left and stop. ("22")
b. If the right is less than the left, stop.
c. If the right is equal to the left, repeat step 3 with the second-last digit in the left and the second digit in the right (and so on).
d. Take the left half and append the left half reversed. That's your next largest palindrome. ("2222")

"""


# lex_auth_01269443664174284882
def nearest_palindrome(number):
    count = 0
    str_num = str(number)
    str_num_list = []
    str_num = str_num[::-1]

    if str(number) == str_num:
        counter = 0
        str_num_list_9 = [x for x in str_num]
        for i in str_num_list:
            if int(i) == 9:
                counter += 1
        if counter == len(str_num_list_9):
            str_num = str(number + 1)
            ls = [x for x in str_num]
            ls[len(str_num)-1] = "1"
            str_num = "".join(ls)
            return str_num

    if len(str_num) % 2 != 0:
        length = len(str_num) // 2
        for i in range(0, length + 1):
            str_num_list.append(str_num[i])
        print(str_num_list)
        str_num_start = str_num[0:length]
        print(str_num_start)
        str_num_end = str_num_start[::-1]
        print(str_num_start)
        # if int(str_num[length]) <= int(str_num[length + 1]):
        str_num_list[length] = str(int(str_num_list[length]) + 1)
    else:
        length = len(str_num) // 2 - 1
        for i in range(0, length + 1):
            str_num_list.append(str_num[i])
        str_num_start = str_num[0:length + 1]
        str_num_end = str_num_start[::-1]
        if str_num[length] < str_num[length + 1]:
            str_num_list[length] = str(int(str_num_list[length]) + 1)
            str_num_start = "".join(str_num_list)
            str_num_end = str_num_start[::-1]
        elif str_num[length] == str_num[length + 1]:
            print("Tes")
            str_num_list_2 = [x for x in str_num]
            a = length
            b = length + 1
            print(a,b)
            while a >= 0 and b <= len(str_num) - 1:
                if str_num[a] > str_num[b]:
                    str_num_list_2[b] = str_num[a]
                    a -= 1
                    b += 1
                elif str_num[b] > str_num[a]:
                    str_num_list_2[a] = str_num[b]
                    a -= 1
                    b += 1
                else:
                    a -= 1
                    b += 1

            str_num = "".join(str_num_list_2)
            return int(str_num)

    for i in range(length + 1, len(str_num)):
        str_num_list.append(str_num_end[count])
        count += 1
    str_num = "".join(str_num_list)
    return int(str_num)


number = 5246
print(nearest_palindrome(number))


"""
def nearest_palindrome(number):
    number=number+1
    s=str(number)
    while(s!=s[::-1]):
        number=number+1
        s=str(number)
    return number

number=12525
print(nearest_palindrome(number))
"""