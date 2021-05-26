# lex_auth_01269438070259712046

def count_names(name_list):
    count1 = 0
    count2 = 0

    for i in name_list:
        if i.find("at") == 1 and i.index("at") + 1 == len(i) - 1:
            count1 += 1
        if i.find("at") != -1:
            count2 += 1
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ", count1)
    print("%at% -> ", count2)


# Provide different names in the list and test your program
name_list = ["Hat", "Cat", "rabbit", "matter"]
count_names(name_list)