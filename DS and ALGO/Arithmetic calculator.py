# # Program to create a small arithmetic Calculator
#
# def Arithmetic_Operation():
#     a = int(input("Enter the first number"))
#     b = int(input("Enter the second number"))
#     ch = 0
#     while ch!= 5:
#         ch = int(input(
#             "\n\nWhich Operation u would wanna perform?: \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Exit\nWnter your choice here: \n\n"))
#         if ch == 1:
#             print("The Addition of ",a," and ",b," is ",a+b)
#         elif ch == 2:
#             print("The Substraction of ",a," and ",b," is", a-b)
#         elif ch ==3:
#             print("The Multiplication of ",a," and ",b," is ", a*b)
#         elif ch == 4:
#             print("The Division of ",a," and ",b," is ", a/b)
#         else:
#             break;
#
#
# Arithmetic_Operation()


# Program for finding the Factors of any given number
# def findFactors(n):
#     print("Factors of ",n," are: ")
#     for i in range(2,n):
#         if n % i == 0:
#             print(i, end = " ")
#     print(n)
#
#
# n = int(input("Enter an Integer: "))
# findFactors(n)


# Program to find Fibonacci series

def Fibonacci(n):
    sum = 0
    for i in range(n):
        sum = sum + i
        print(sum, end=" ")


Fibonacci(10)