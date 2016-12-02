class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# HEAD
#
# Given the head of a linked list and an int, append a node with the int data to the head of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 5 -> 1 -> 2 -> 3 -> 4 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the head node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the head
def add_head(head, n):
    if head==None: #If list is empty
        head=Node(n,None)
        return head
    original=head 
    head=Node(n,original) #make new node and attach its next to the rest of the list
    return head
