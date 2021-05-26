# lex_auth_012742478130135040816

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    # adding element before3 specified data
    def add_after_data(self,key,data):
        new_node = Node(data)
        if self.__head == None:
            return "List is Empty"
        else:
            temp = self.__head
            while temp is not None:
                if temp.get_data() == key:
                    if temp == self.__tail:
                        temp.set_next(new_node)
                        self.__tail = new_node
                        return "Added Successfully at the end"
                    else:
                        new_node.set_next(temp.get_next())
                        temp.set_next(new_node)
                        return "Added Successfully in begining"
                temp = temp.get_next()
            return "No such data available"


    # You can use the below __str__() to print the elements of the DS and ALGO object while debugging
    def show(self):
        temp = self.__head
        print(temp)
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()



def count_nodes(biscuit_list):
    count = 0
    temp = biscuit_list.get_head()
    while (temp is not None):
        temp = temp.get_next()
        count += 1
    return count


biscuit_list = LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

print(biscuit_list.add_after_data("Goodday","ABC"))
biscuit_list.show()
