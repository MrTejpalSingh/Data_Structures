# Trying another Pattern (Pyramid Top Left Pattern)
num = int(input("Enter an Integer here--> "))
for i in range(1,num+1):
    if i == num:
        for k in range(1,num+1):
            print("*", end=" ")
    for j in range(1,num+1-i):
        print(" ",end = " ")
        if j == num-i:
            sp = j+1
            while sp <= num:
                print("*",end=" ")
                sp += 1
    print()