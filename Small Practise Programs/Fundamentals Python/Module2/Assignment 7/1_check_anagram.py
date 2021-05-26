#lex_auth_0127382206342184961397
def check_anagram(data1,data2):
    # A lsit to strore wheather or not the second string chars were checked

    second_str_ind = []
    for i in range(0,len(data2)):
        second_str_ind.append(0)
    print(second_str_ind)
    # It should initially have all zeros'c
    # since no comparison performed yet

    counter = 0

    if len(data1) == len(data2):
        for i in range(0,len(data1)):
            for j in range(0,len(data2)):
                if data1[i] == data2[j].lower() or data1[i] == data2[j].upper():
                    if i == j:
                        counter = 0
                    else:
                        if second_str_ind[j] == 0:
                            second_str_ind[j] = 1
                            counter += 1
                            break
    print(counter,len(data1))
    if counter != len(data2):
        return False
    else:
        return True

# print(check_anagram("Reductions","discounter"))

print(check_anagram("backward","drawback"))