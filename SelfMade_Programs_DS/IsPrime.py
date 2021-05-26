def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

ch = 1
while ch!= 2:
    ch = int(input("\n1) Wanna check for another number \n2) Exit\n Enter your choie here--> "))
    if ch == 1:
        a = int(input("\nEnter an Integer here--> "))
        if isPrime(a):
            print("\n          _[",a, " is a Prime Number.]_")
        else:
            print("\n          _[",a, " is Not a Prime Number.]_")
    elif ch == 2:
        break
    else:
        print("\n          _[Enter a Valid Choice!]_")


