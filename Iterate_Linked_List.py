class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# ITERATE
#
# Given the head of a linked list, iterate through the linked list and print the values.
#
# Note: THIS IS A COMPLETED EXAMPLE FOR YOU
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       1, 2, 3, 4
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
#   None, prints values
#
def iterate(head):
    while(head != None):
        print head.data
        head = head.next
