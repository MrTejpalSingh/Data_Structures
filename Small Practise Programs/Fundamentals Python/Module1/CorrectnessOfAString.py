# lex_auth_01269444890062848087
"""
--------------------------------------------------Solution of an advanced problem---------------------------------------
"""
# def find_correct(word_dict):
#     list_of_ans = []
#     correct = 0
#     al_correct = 0
#     wrong = 0
#     for key, value in word_dict.items():
#         if len(key) != len(value):
#             wrong += 1
#         elif key == value:
#             correct += 1
#         else:
#             key_str = key
#             val_str = value
#             counter = 0
#     ------[ for j in key_str:
#                 if j in val_str:
#                     counter += 1 ]------ changed part
#             if counter >= len(key) - 2:
#                 al_correct += 1
#             else:
#                 wrong += 1
#     list_of_ans = [correct, al_correct, wrong]
#     return list_of_ans


"""
---------------------------------------------Solution of actual problem----------------------------------------------------
"""

def find_correct(word_dict):
    list_of_ans = []
    correct = 0
    al_correct = 0
    wrong = 0
    for key, value in word_dict.items():
        if len(key) != len(value):
            wrong += 1
        elif key == value:
            correct += 1
        else:
            key_str = key
            val_str = value
            counter = 0
            for j in range(len(key_str)):
                if key_str[j] == val_str[j]:
                    counter += 1
            if counter >= len(key) - 2:
                al_correct += 1
            else:
                wrong += 1
    list_of_ans = [correct, al_correct, wrong]
    return list_of_ans

word_dict = {"MOST": "MICE", "THREE": "TRICE", "COME": "COME", "GET": "GOT"}
print(find_correct(word_dict))