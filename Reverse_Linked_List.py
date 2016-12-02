class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# REVERSE
#
# Given the head of a linked list, return a linked list that is reversed.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 4 -> 3 -> 2 -> 1 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# head: node
#   Head of the reversed linked list
def reverse(head):
    if head == None: #If Linked List is empty
        return None
    if head.next==None: # If only one element in the list
        return head
    previous_node = None #Stores the link to the previous node
    current_node = head
    while(current_node is not None): #Iterate through the linked list
        next = current_node.next # assign next to current node's next
        current_node.next = previous_node #assign current node's next to  previous node
        previous_node = current_node
        current_node = next
        head = previous_node
    return head