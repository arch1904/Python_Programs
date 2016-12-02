class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# ADD
#
# Given the head of a linked list, an int : data and an int : i, add a node with int : data to the i'th position in the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 5 -> 4 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# data : int
#   data for the tail node
#
# i : int
#   position of the new node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node in the i'th position of the linked list
def add_position(head, data, i):
    if i<0: #If given index is negative return None
        return None
    if head is None: #If list is empty add item to default 0th index
        head=Node(data,None)
        return head
    if i==0: #if user wants to append to the head use add_head
        return add_head(head,data)
    count=-1 #counter for number of nodes
    current_node=head
    prev=head
    while current_node is not None:
        count+=1
        if(count==i): #iterate through list to get to i'th position
            prev.next=Node(data,current_node)
            return head
            break
        else:
            prev=current_node
            current_node=current_node.next
    if i>count: #If i is greater than the number of nodes in the list add to the end
        return add_tail(head,data)
    return None

