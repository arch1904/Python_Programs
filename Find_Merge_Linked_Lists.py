class linked_node(object):
    # Node class for linked list implementation
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# Find Merge Point
#
# Given the head of two linked lists that are merged, return the data at the node where the two lists merge.
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
# Returns
# -------
# int: data
#   data at merge node
def findMerge(head_a, head_b):
    curr_a=head_a
    curr_b=head_b
    data_a ={}
    while(curr_a.next is not None):
        data_a[curr_a]=0
        curr_a=curr_a.next
    while(curr_b.next is not None):
        if curr_b in data_a.keys():
            return curr_b.data
        curr_b=curr_b.next
    return None