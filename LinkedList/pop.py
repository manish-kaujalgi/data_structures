### To remember -
### 1. Need to point the tail to the last-but-one item and remove the last node (to POP)
### 2. The EDGE CASES - 
###     a. If LL is empty
###     b. If LL has only 1 item




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


# my_linked_list = LinkedList.append(0, 9)

my_linked_list = LinkedList(4)

my_linked_list.append(9)

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

# my_linked_list.print_list()
# print(my_linked_list.head.value)