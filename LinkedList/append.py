### PROPERTIES of LL -
### 1. It does not have a index unlike a `List`
### 2. They are not next to 1 another in the memory and will have a reference linking to the next item, thereby making it a LL
### 3. It has 2 properties (remember the DICTIONARY setup) - `value` and `next` along with `HEAD` and `TAIL`


### To remember -
### 1. Need to point the last item of the existing LL to the new node and move the tail to this node
### 2. The EDGE CASE - If LL is empty, need to point the head and tail to the new node added




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


# my_linked_list = LinkedList.append(0, 9)

my_linked_list = LinkedList(4)

my_linked_list.append(9)

my_linked_list.print_list()
# print(my_linked_list.head.value)