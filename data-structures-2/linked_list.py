class Node:
    def __init__(self, val):
        val = val
        next = None
    
    def set_next(self, next):
        next = next
    


# Creating a node
head = Node("hello")

head.set_next(Node("world"))

desired_node = head.next 
desired_node.val = "world"

