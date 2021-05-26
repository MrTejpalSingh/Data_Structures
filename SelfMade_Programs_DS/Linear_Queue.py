# Trying to implement Linear Queue Data structure
# with POP (Procedural Oriented Programming) in Python

rear = -1
front = -1
max = 4
MyQueue = []
# Inserting an element into the queue
def enqueue(val):
    global rear
    global front
    if rear == front == -1:
        rear += 1
        front += 1
        MyQueue.append(val)
        print("\nAddded: ", val,"Rear:",rear,"   QueueIndex:",MyQueue.index(MyQueue[rear]),"\n")
    else:
        rear += 1
        MyQueue.append(val)
        print("\nAddded: ", val,"Rear:",rear,"   QueueIndex:",MyQueue.index(MyQueue[rear]),"\n")

def deqeue():
    global rear
    global front
    print("\nRemoved: ",MyQueue[front],"front:",front,"   QueueIndex:",MyQueue.index(MyQueue[front]),"\n")
    front += 1

def display():
    print("\nQueue: ",end= " [ ")
    for i in range(front, rear+1):
        print(MyQueue[i],end= " ")
    print("] ")

def IsFull():
    if rear == max-1:
        return True
    return False

def IsEmpty():
    if front == -1 or front > rear:
        return True
    return False

# enqueue(78)
# enqueue(33)
# enqueue(1)
# enqueue(5)
# display()
# enqueue(11)
# deqeue()
# deqeue()
# deqeue()
# deqeue()
# deqeue()

ch = 0
while ch != 2:
    ch = int(input("\nChoose from the following\n1) Create a new Queue\n2) Exit\nEnter your choice is here----> "))
    if ch == 2:
        break
    elif ch == 1:
        max = int(input("what should be the capacity of the queue:---> "))
        ch = 0
        while ch != 4:
            ch = int(input("\nChoose from the following\n1) Add an element\n2) Delete an element\n3) Dispaly Queue\n4) Exit\nEnter your choice here---> "))

            if ch == 1:
                if IsFull():
                    print("\nQueue is Full\n")
                else:
                    val = int(input("Enter an Integer---> "))
                    enqueue(val)
            elif ch == 2:
                if IsEmpty():
                    print("\nQueue is Empty!\n")
                else:
                    deqeue()
            elif ch == 3:
                if IsEmpty():
                    print("Queue is Empty!")
                else:
                    display()
            elif ch == 4:
                break
            else:
                print("Enter a valid choice!....")

