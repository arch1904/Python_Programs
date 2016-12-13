class linked_node(object):
    # Node class for linked list implementation
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# Merge
#
# Given the head of two linked lists, return true if the linked lists merge, and false if they do not merge.
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head_a : node
#   Head of a linked list
#
# head_b : node
#   Head of another linked list
#
#
# Returns
# -------
#   Boolean
#
def isMerged(head_a, head_b):
    curr_a=head_a
    curr_b=head_b
    while curr_a.next is not None:
        curr_a=curr_a.next
    while curr_b.next is not None:
        curr_b=curr_b.next
    if(curr_a.data==curr_b.data and curr_a.next==curr_b.next):
        return True
    return False