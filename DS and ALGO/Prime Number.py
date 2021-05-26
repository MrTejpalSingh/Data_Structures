# Program for finding the Prime number
def IsPrimeNo(n):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
    if flag == 0:
        print(n," is a Prime Number!")
    else:
        print(n, " is not a Prime Number!")

number = int(input("Enter an Integer!"))
IsPrimeNo(number)