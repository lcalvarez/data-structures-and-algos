class Node():
    def __init__(self, val, next_val=None):
        self.val = val
        self.next = next_val

def find_first_occurrence(ll, val):
    if ll is None:
        return -1

    curr = ll
    idx = 0
    while curr is not None:
        curr_val = curr.val
        if val == curr_val:
            return idx

        idx += 1
        curr = curr.next

    return -1

list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
list2 = Node(2)
list3 = Node(-1, Node(-2, Node(-3, Node(-4, Node(-5)))))
list4 = Node(1, Node(2, Node(3, Node(2, Node(1)))))

print(find_first_occurrence(None, 12) == -1)
print(find_first_occurrence(list1, 9) == -1)
print(find_first_occurrence(list1, 3) == 2)
print(find_first_occurrence(list2, 2) == 0)
print(find_first_occurrence(list2, 1) == -1)
print(find_first_occurrence(list3, -2) == 1)
print(find_first_occurrence(list4, 2) == 1)
print(find_first_occurrence(list4, 1) == 0)
