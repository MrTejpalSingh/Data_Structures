# lex_auth_01269444961482342489

def sms_encoding(data):
    list_msg = data.split(" ")
    vowels_set = set("aeiouAEIOU")
    for i in range(0, len(list_msg)):
        count = 0
        for j in list_msg[i]:
            if j in vowels_set:
                count += 1
        if count == len(list_msg[i]):
            pass
        else:
            str_word = ""
            list_msg_sb = []
            for j in list_msg[i]:
                list_msg_sb.append(j)
            j = 0
            while j < len(list_msg_sb):
                if list_msg_sb[j] in vowels_set:
                    list_msg_sb.remove(list_msg_sb[j])
                else:
                    j += 1

            str_word = "".join(list_msg_sb)
            list_msg[i] = str_word


    data = " ".join(list_msg)
    return data


data = "I love Python"
print(sms_encoding(data))