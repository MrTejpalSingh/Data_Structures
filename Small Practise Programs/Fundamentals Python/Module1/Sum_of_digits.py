def find_sum_of_digits(number):
    sum_of_digits=0
    while number!= 0:
        last_digit = number % 10
        number = number // 10
        sum_of_digits = sum_of_digits + last_digit
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(564)
print("Sum of digits:",sum_of_digits)