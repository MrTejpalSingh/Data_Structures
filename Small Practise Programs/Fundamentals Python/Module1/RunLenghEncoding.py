# lex_auth_012693816331657216161

def encode(message):
    encoded_msg = ""
    i = 0
    while i <= len(message)-1:
        if i == len(message)-1:
            encoded_msg = encoded_msg + "1" + message[i]
            i += 1
        else:
            j = i + 1
            counter = 1
            while message[j] == message[i]:
                counter += 1
                j += 1
            encoded_msg = encoded_msg + str(counter) + message[i]
            i = j
    return encoded_msg
# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)