class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# TAIL
#
# Given the head of a linked list and an int, append a node with the int data to the tail of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 5 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the tail node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the tail
def add_tail(head, n):
    if head==None: #If list is empty 
        head=Node(n,None)
        return head
    current_node=head 
    while current_node.next is not None: #Iterate to end of the list
        current_node=current_node.next
    current_node.next=Node(n,None) #Add the new node
    return head
