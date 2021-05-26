#lex_auth_01269446319507046499

def remove_duplicates(value):
    list_distinct = []
    for i in value:
        if i not in list_distinct:
            list_distinct.append(i)
    return "".join(list_distinct)


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))