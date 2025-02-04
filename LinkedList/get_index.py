### To remember -
### We need to always return the entire NODE. Not just the value.
### We are using the temp.value to return and print for the validation purposes




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node_append = Node(value)

        if self.head is None:
            self.head = node_append
            self.tail = node_append
        else:
            self.tail.next = node_append
            self.tail = node_append

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:  ### OR also we can do if HEAD / TAIL is NONE 
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None: ### OR also we can do while(temp.next): ## is true
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        # print(temp.value)
        return temp.value
    
    def prepend(self, prepend_value):
        new_node = Node(prepend_value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

        return True
    
    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

my_linked_list = LinkedList(4)

my_linked_list.append(9)
my_linked_list.prepend(6)
my_linked_list.print_list()

print(my_linked_list.get_index(0).value)
# print(my_linked_list.head.value)