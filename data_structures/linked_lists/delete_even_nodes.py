
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteEvenNodes(head):
    if head is None:
        return head
    
    dummyNode = Node(0)
    dummyNode.next = head
    current = dummyNode
    
   # D --> Head(2) --> 2 --> 2 
   # c.    nxt
   # D --> 2 
   
    while current is not None and current.next is not None:
        # Check if head is even

        if current.next.val % 2 == 0:
            current.next = current.next.next

        current = current.next

    if dummyNode.next.next is None and dummyNode.next.val % 2 == 0:
        return Node(None)
    
    return dummyNode.next


def print_ll(node):
    current = node
    while current is not None:
        print(f"{current.val}")
        print("\n")
        current = current.next


# Test cases

'''
EXAMPLE(S)
[3,1,3] => [3, 1, 3]
[5, 6, 9] => [5, 9]
[2, 2, 2] => []
[2, 7, 4, 3, 5] => [7, 3, 5]
'''

ll = Node(3)
ll.next = Node(1)
ll.next.next = Node(3)
print_ll(ll)
new_list = deleteEvenNodes(ll)
print_ll(new_list)
print("New call")

# [5, 6, 9]
ll = Node(5)
ll.next = Node(6)
ll.next.next = Node(9)

print_ll(ll)
new_list = deleteEvenNodes(ll)
print_ll(new_list)
print("New call")


ll = Node(2)
ll.next = Node(2)
ll.next.next = Node(2)
print_ll(ll)
new_list = deleteEvenNodes(ll)
print("Output list")
print_ll(new_list)
print("New call")

def traversal(ll):
    # base case
    if ll is None:
        return
        
    print(ll.val)
    traversal(ll.next)
