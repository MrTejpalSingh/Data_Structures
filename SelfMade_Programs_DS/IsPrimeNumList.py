def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
ch = 1
while ch != 2:
    ch = int(input("\n1) Wanna check for another number\n2) Exit\n Enter your choice--> " ))
    if ch == 1:
        a = int(input("Enter an integer here---> "))
        for i in range(2, a + 1):
            if isPrime(i):
                print(i, end=" ")
    elif ch == 2:
        break
    else:
        print("\n Enter a Valid Choice!")
