"""
@author: Piyush Basak
"""


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def insert_in_emptylist(self):
        if self.start_node is None:

            num = input('Enter data:')
            new_node = Node(num)
            self.start_node = new_node
        else:
            print("list is not empty")


new_linked_list = LinkedList()
new_linked_list.insert_in_emptylist()
new_linked_list.insert_at_start(71)
new_linked_list.insert_at_start(39)
new_linked_list.insert_at_end(100)
new_linked_list.insert_at_end(201)

new_linked_list.traverse_list()
n = new_linked_list.get_count()
print("This list has", n, "number of elements")
