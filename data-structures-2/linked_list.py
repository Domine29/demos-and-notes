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

head = Node("hello")
temp_node = Node("world")
head.set_next(temp_node)

# print(head.next)
head.next.set_next(Node("its sunny"))

# print(head.next.next)
head.next.next.set_next(Node("but cold!"))

current_node = head

# Use these for an example list of just one thing
# new_head = Node("list with one thing")
# current_node = new_head

while(current_node != None):
    print("current node: " + current_node.val)
    # When we are at the tail, this throws an error because `next` does not exist
    if current_node.next != None:
        print("next node: " + current_node.next.val)
    else:
        print("welcome to the tail!")
    print(" ")
    current_node = current_node.next # For tail, current_node.next == None
