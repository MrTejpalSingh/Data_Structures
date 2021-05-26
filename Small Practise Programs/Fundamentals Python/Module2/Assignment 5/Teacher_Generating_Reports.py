#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum = 0
    for i in list_of_marks:
        sum += i
    average = sum / len(list_of_marks)
    count = 0
    for i in list_of_marks:
        if i > average:
            count += 1
    return (count * 100) / len(list_of_marks)

def sort_marks():
    marks = list(list_of_marks)
    marks.sort()
    return marks

def generate_frequency():
    freq_count = []
    for i in range(0, 26):
        if i in list_of_marks:
            freq_count.append(list_of_marks.count(i))
        else:
            freq_count.append(0)
    return freq_count



print(find_more_than_average())
print(generate_frequency())
print(sort_marks())