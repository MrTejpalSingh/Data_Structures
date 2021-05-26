#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    merged_data=""
    resultant_data = []
    i = 0
    j = -1
    while i <= len(list1) - 1:
        while j >= - (len(list2)):
            if list2[j] == None:
                resultant_data.append(list1[i])
            elif list1[i] == None:
                resultant_data.append(list2[j])
            else:
                resultant_data.append(list1[i] + list2[j])
            i += 1
            j -= 1
    merged_data = " ".join(resultant_data)
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)