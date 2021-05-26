#lex_auth_01269443477535129681

def find_dup(list_of_numbers):
    if len(list_of_numbers) > 0:
        temp = list_of_numbers[0]
        list_of_numbers.remove(temp)
        if temp in list_of_numbers:
            for i in list_of_numbers:
                if temp == i:
                    list_of_numbers.remove(i)
            return str(temp ) + " " + str((find_dup(list_of_numbers)))
        else:
            return find_dup(list_of_numbers)
    else:
        return ""

def find_duplicates(list_of_numbers):
    list_of_duplicates = find_dup(list_of_numbers)
    str_str = ""
    lsdts = []
    for i in range(0,len(list_of_duplicates)-1):
        if type(list_of_duplicates[i]) != str:
            list_of_duplicates[i] = str(list_of_duplicates[i])
        if list_of_duplicates[i].isdigit():
            str_str = str_str + list_of_duplicates[i]
            print(str_str)
            print(list_of_duplicates[i + 1])
            if list_of_duplicates[i + 1].isdigit() == False:
                lsdts.append(int(str_str))
                str_str= ""
                print("This is appended value:- ",str_str)
                continue

    print("Final___list",lsdts)
    return lsdts

list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)