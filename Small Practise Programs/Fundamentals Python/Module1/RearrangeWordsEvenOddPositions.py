#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=sentence.split()
    for i in range(0,len(word)):
        if((i%2)==0):
            final_list.append(word[i][::-1])
        else:  # do rearrangement
            vowels = list()
            consonants = list()
            for letter in word[i]:
                if letter in vowel_set:
                    vowels.append(letter)
                else:
                    consonants.append(letter)
            new_string = "".join(consonants) + "".join(vowels)
            final_list.append(new_string)
    sentence = " ".join(final_list)
    return sentence

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)