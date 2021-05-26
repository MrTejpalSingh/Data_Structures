# lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    if no_of_people == 1:
        return 50
    else:
        return no_of_people * 50 + human_pyramid(no_of_people - 2)


def find_maximum_people(max_weight):
    no_of_people = max_weight // 50
    if no_of_people % 2 == 0:
        no_of_people -= 1
    weight = human_pyramid(no_of_people)

    while weight >= max_weight:
        if weight == max_weight:
            break
        no_of_people -= 2
        weight = human_pyramid(no_of_people)

    return no_of_people


# Provide different values for max_weight and test your program
max_people = find_maximum_people(200)
print(max_people)