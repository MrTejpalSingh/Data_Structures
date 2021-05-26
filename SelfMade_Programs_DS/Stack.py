# Trying to implement Stack Data structure
# with POP (Procedural Oriented Programming) in Python
top = -1
Max = 4
def Push(val):
    global top
    global Max
    if top >= Max:
        print("Stack Overflow")
    else:
        top += 1
        stackUser.append(val)
        print("Added: ",val)
def Pop():
    global top
    if top <= -1:
        print("Satck Underflow")
    else:
        print("Removed: ",stackUser[top])
        stackUser.remove(stackUser[top])
        top -= 1

def display():
    global top
    if top <= -1:
        print("Stack is empty")
    else:
        print("Stack: [ ",end=" ")
        for i in range(0,top+1):
            print(stackUser[i],end=" ")
        print(" ] ")


ch = 0
while ch != 2:
    ch = int(input("What do u wanna do.....Choose from below options\n1) Create a new Stack \n2) Exit\n---->"))
    if ch != 2 and ch != 1:
        print("Enter a valid choice")
    elif ch == 2:
        break
    else:
        # Creation of a stack
        stackUser = []
        Max = int(input("How many elements would u wanna store into the stack")) - 1
        ch2 = 0
        while ch2 != 4:
            ch2 = int(input("\nChoose any of the following: \n1) PUSH\n2) POP\n3) DISPLAY\n4) Exit\nEnter your choice here(in number(1-4)):- " ))
            if ch2 == 1:
                val = int(input("Please enter an integer here to added: "))
                Push(val)
            elif ch2 == 2:
                Pop()
            elif ch2 == 3:
                display()
            elif ch2 == 4:
                break
            else:
                print("Please enter a valid choice!\n")




