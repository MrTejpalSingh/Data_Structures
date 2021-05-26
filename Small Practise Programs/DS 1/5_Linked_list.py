"""
This is will only give u an idea of how a linked list works rather than being an exact solution
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_beg(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        if self.head == None:
            print("List is Empty!")
        else:
            temp = self.head
            while temp.next != None:
                print(temp.data)
                temp = temp.next
            print(temp.data)

ll1 = LinkedList()
ll1.add_to_end(50)
ll1.add_to_end(10)
ll1.add_to_end(20)
ll1.add_to_end(54)

ll1.add_beg(88)
ll1.add_beg(66)

ll1.traverse()