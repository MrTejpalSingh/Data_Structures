# lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    word_freq_dict = {}

    list_data = data.split(" ")
    for i in list_data:
        frequency = 0
        for j in list_data:
            if i == j:
                frequency += 1
                # print(i, j, frequency)
                word_freq_dict[i] = frequency

    length = 0
    maximum = max(word_freq_dict, key=word_freq_dict.get)
    for key in word_freq_dict:
        if word_freq_dict[maximum] == word_freq_dict[key]:
            if len(key) > length:
                length = len(key)
                word = key
    # # length = 0
    # # for key, value in word_freq_dict.items():
    # #     if max_val == word_freq_dict[key]:
    # #         if len(key) > length:
    # #             length = len(word_freq_dict)
    # #             word = key
    #
    # for key, vale in word_freq_dict.items():
    #     if word == key and length == len(word_freq_dict):
    #         word = key
    #         frequency = word_freq_dict[key]
    word = word + " " + str(word_freq_dict[word])
    print(word)


# Use the below given print statements to display the output
# Also, do not modify them for verification to work


# Provide different values for data and test your program.
data = "Hands to clap and eyes to see"
# data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
