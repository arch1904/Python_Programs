class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node



# DELETE
#
# Given the head of a linked list, an int : i, delete the i'th node in the linked list and return the new linked list.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# i : int
#   position of the node to delete
#
# Returns
# -------
# head : node
#   Head of a linked list with the node in the i'th position of the linked list deleted
def delete(head, i):
    if head==None: #If list is empty
        return None
    if i==0: #if user wants to delete the first node
        return head.next
    current_node=head
    count=-1 #counter for nodes
    prev = None
    while current_node is not None: 
        count+=1
        if count==i: #iterate till i'th position
            prev.next=current_node.next #assign previous node's next to current node's next
            break
        else:
            prev=current_node
            current_node=current_node.next
    return head
