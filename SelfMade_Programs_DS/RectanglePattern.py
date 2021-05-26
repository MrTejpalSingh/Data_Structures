# Rectangle Patter Printing
print("Printing a Rectangle Pattern: ")
row,col = [int(x) for x in input().split()]
for i in range(0,row):
    for i in range(0,col):
        print("*",end=" ")
    print("")
