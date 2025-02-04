### PROPERTIES of LL -
### 1. It does not have a index unlike a `List`
### 2. They are not next to 1 another in the memory and will have a reference linking to the next item, thereby making it a LL
### 3. It has 2 properties (remember the DICTIONARY setup) - `value` and `next` along with `HEAD` and `TAIL`


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


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)