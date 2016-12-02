class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node



# DELETE_DUPLICATE
#
# Given the head of a linked list, delete all consecutive duplicate nodes in the linked list. Only consider CONSECUTIVE duplicates.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 2 -> 3 -> 4 -> 2 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 2 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# Returns
# -------
# head : node
#   Head of a linked list with the node with consecutive duplicates deleted.
def deleteDuplicate(head):
    if head==None: #If list is empty
        return None
    current_node=head
    values_parsed={} #dictionary to hold values parsed
    prev=None
    while(current_node is not None): #Iterate through the list
        if current_node.data in values_parsed:
            prev.next=current_node.next # if duplicate found then delete
        else:
            values_parsed[current_node.data]=0 #add value to values parsed
            prev=current_node
        current_node = current_node.next
    return head 




