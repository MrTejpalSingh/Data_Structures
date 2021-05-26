#lex_auth_012694465248329728100

def validate_name(name):
    if len(name) == 0:
        return False
    else:
        if len(name) > 15:
            return False
        else:
            if name.isalpha():
                return True
            else:
                return False

def validate_phone_no(phno):
    str_num = str(phno)
    if len(str_num) == 10:
        if str_num.isdigit():
            for i in range(0,len(str_num)):
                if str_num[i] != str_num[0]:
                    return True
            return False
        else:
            return False
    else:
        return False

def validate_email_id(email_id):
    if "@" and ".com" not in email_id:
        return False
    else:
        username_domain = email_id.split("@")
        if ".com" not in username_domain[0]:
            if ".com" != email_id[-4:]:
                return False
            else:
                doamin = ["gmail", "yahoo", "hotmail"]
                if email_id[email_id.index("@") + 1:-4] not in doamin:
                    return False
                else:
                    return True
        else:
            return False

def validate_all(name,phone_no,email_id):
    count = 0
    if validate_name(name):
        # print("valid Name")
        count += 1
    else:
        print("Invalid Name")

    if validate_phone_no(phone_no):
        # print("valid phone number")
        count += 1
    else:
        print("Invalid phone number")

    if validate_email_id(email_id):
        # print("valid email id")
        count += 1
    else:
        print("Invalid email id")

    if count == 3:
        print("All the details are valid")



#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9998459998", "tom.com@yahoo.com")
# print(validate_phone_no(9999999999))