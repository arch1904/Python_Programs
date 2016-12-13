class tree_node(object):
    # Node class for BST implementation
    def __init__(self, data=None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


# Find Odd
#
# Given the head node of a BST, return all odd data members of nodes in the tree in a list.
# Duplicates must be considered. Order does not matter.
#
#
# Example(s)
# ----------
# Input (tree representation):
#   head: node
#
#            3
#          /   \
#         2     5
#        / \   / \
#       4   3 8   7
#
# Output:
#   odds: list
#   [3,5,3,7]
#
#
# Parameters
# ----------
# head : node
#   Head of a BST
#
#
# Returns
# -------
# odds : list
#   list of odd data members in the tree

def make_list(head):
    if head:
        s = ""
        if(head.data%2!=0):
            s=str(head.data)
        if head.left and head.right:
            return s + " "+ make_list(head.left)+  " " + make_list(head.right)
        elif head.left:
            return s + " "+ make_list(head.left)
        elif head.right:
            return s + " "+ make_list(head.right)
        else:
            return s
def findOdd(head):
    if not head: #if root node doesnt exist
        return None
    l=[]
    s = make_list(head) #returns a string with all odd elements
    l=s.split() #list of chars
    for i in range(0,len(l)):
        l[i]=int(l[i]) #required list of numbers
    return l