class linked_node(object):
    # Node class for linked list implementation
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Cycle
#
# Given the head of a linked list, find out whether or not there is a cycle.
#
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# boolean :
#   True if there is a cycle, False if there is not
def foundCycle(head):
    #Using Tortoise and Hare method
    if(head is None):
         return False
    if(head.next is None):
         return False
    tortoise = head
    hare = head
    while(tortoise is not None and hare is not None):
        tortoise=tortoise.next
        if(hare.next is None):
            break;
        hare=hare.next.next
        if(hare.data==tortoise.data and hare.next==tortoise.next):
            return True
    return False
