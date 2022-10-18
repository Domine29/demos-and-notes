# Linked list is a chain of node objects
# A 'node' is the just the name we use for a thing in the list

# What can we do with a linked list?
# Insert node / create new node
# Delete node
# Find a node --> traverse the list 
# Replace a node
#   - This a more sophisticated operation

# Two special nodes in the linked list:
# Head --> first node in the list
#   - We need have access to the head so we have access to the list 
# Tail --> last node in the list
#   - We need to know which node is the tail so we know when to stop

# value
# pointer to the next node in the list 


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.val

    def set_next(self, next):
        self.next = next

    # Check if self.next has a value or not
    # def is_tail(self):
    #     return self.next == None
# Print all nodes
# Add node
# Remove node
# Get specific node
#
#
#

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_nodes(self):
        current = self.head
        while(current != None):
            print(current.val)
            current = current.next

    # Add head
    # Add anything other than the head
    def add(self, node):
        # Node is head
        if(self.head == None):
            # print("Adding as head")
            self.head = node
            self.tail = node

        # If Node is not head, add to end of list
        else:
            # Adds new node to end of list
            self.tail.next = node

            # Keeps track of the tail
            self.tail = node



list = LinkedList()

# Very first node
# List length is 1
# "hello" is the head ... and tail!

"hello"
list.add(Node("hello")) 

# "hello", "world"
list.add(Node("world"))

# "hello", "world", "its sunny"
list.add(Node("its sunny"))

# "hello", "world", "its sunny", "but cold"
list.add(Node("but cold"))

list.print_nodes()