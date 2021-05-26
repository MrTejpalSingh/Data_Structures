# ________________________________________________________
#
#
#                     ON HOLD
#
#
# ________________________________________________________


# # Program of finding the list of prime numbers
#
# def ListOfPrimeNos(n):
#     flag = 'NP'
#     prime_numbres = []
#     for i in range(2,n):
#         print("for ",i," in range(2,",n,"):")
#         for j in range(2,i):
#             print("    for ",j," in range(2,",i,"):")
#             if i % j == 0:
#                 print("        if ",i," % ",j," == 0:")
#                 flag = 'P'
#                 print("            flag = 'P'")
#         if flag == 'NP':
#             print("    if flag == 'NP':")
#             prime_numbres.append(i)
#             print("prime_numbres.append(",i,")", prime_numbres)
#     return prime_numbres
#
# n = int(input("Enter an Integer: "))
# print("List of Pirme Numbers is: ",ListOfPrimeNos(n))



# Program to find the list of prime numbers

def ListOfPrimeNo(n):
    flag = 0
    for j in range(2,n):
        for i in range(2, j):
            if j % i == 0:
                flag = 1
        if flag == 0:
            print(j, " is prime number")
        else:
            print(j, " is not a Prime number")



number = int(input("Enter an integer: "))
ListOfPrimeNo(number)
