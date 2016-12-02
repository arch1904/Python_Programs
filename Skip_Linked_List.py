class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# SKIP
#
# Given the head of a linked list, return a linked list with every other node
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 3 -> NONE
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
# head : node
#   Head of a linked list with every other node
def skip(head):
    if head == None: #If Linked list is empty
        return None
    if head.next==None: #If linked list has only one node
        return head
    current_node=head
    while current_node is not None and current_node.next is not None: #iterate through list
        current_node.next=current_node.next.next #Skips one node here
        current_node=current_node.next
    return head 
