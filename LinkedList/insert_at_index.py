### Since this is like a dictionary, please remember that any other references pointing to the same dictionary \
###     if updated, will ultimately update the original values in the dictionary


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

    def set_index(self, index, value):
        temp = self.get_index(index)
        if temp:                        ### Also we can write - if temp is not None:
            temp.value = value
            return True 
        return False

    def insert_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        new_node = Node(value)

        temp = self.get_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
            
        self.length += 1
        return True


my_linked_list = LinkedList(11)

my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.insert_index(4, 4)
my_linked_list.print_list()

# print(my_linked_list.head.value)