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


# Iterate through linked list using recursion and print each one out
def print_list_recursive(current_node):
    # Base case - at end of list
    if current_node == None:
        return 

    print(current_node.val)

    # Do the recursion
    # Reecurse with updated value
    next = current_node.next
    return print_list_recursive(next) 

# print_list_recursive(head)


# Get a specific node from linked list
def get_node_recursive(current_node, desired_val):
    # Base cases
    # At end of list - stop recursion
    if current_node == None:
        return None

    # Found desired node - stop recursion
    if current_node.val == desired_val:
        print("match! " + current_node.val + " matches " + desired_val)
        return current_node 
    
    print("checking " + current_node.val)

    # Recursion
    return get_node_recursive(current_node.next, desired_val)

desired_node = get_node_recursive(head, "and getting colder")

print("Haha! I found " + desired_node.val)