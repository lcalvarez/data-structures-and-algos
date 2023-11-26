class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element

    def __str__(self):
        return str(f"Node data is {self.data}")

class LinkedList:
    def __init__(self, node=None):
        self.head_node = node

    def get_head(self):
        return self.head_node

    def traverse(self):
        # Grab the current head node
        current_node = self.head_node

        # Iterate over all entries
        while current_node is not None:
            print(current_node.data)
            print('|')
            current_node = current_node.next_element
            if current_node is None:
                print("Next element is None")

    def is_empty(self):
        if self.head_node is None:
            return True
        
        return False

    def insert_at_head(self, node):
        # Grab the current head node
        current_head = self.head_node
        
        # Set the new node's next element to be the current head
        node.next_element = current_head

        # Now point the head node to the new node
        self.head_node = node

    def get_tail(self):
        pass

    def insert_at_tail(self, node):
        pass

    def find_value(self, data):
        pass

    

if __name__ == '__main__':
    nodes = Node(1, Node(2, Node(3)))
    llst = LinkedList(nodes)
    #print(llst.get_head())
    #print(llst.is_empty())
    print(llst.traverse())
    #llst.insert_at_head(Node(10))
    #print(llst.traverse())
