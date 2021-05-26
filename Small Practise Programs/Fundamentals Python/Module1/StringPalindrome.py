#lex_auth_012693819159732224162
"""
------------------------------------------First Solution-----------------------------
"""
# def check_palindrome(word):
#     liststr = []
#     for i in word:
#         liststr.append(i)
#     liststr.reverse()
#     reversed_word = ""
#     for i in liststr:
#         reversed_word = reversed_word + i
#     if word == reversed_word:
#         return True
#     else:
#         return False

"""
-----------------------------------------Second Solution----------------------------------------
"""

def check_palindrome(word):
    if word[::-1] == word:
        return  True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")