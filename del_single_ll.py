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
            print("The list is:")
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

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

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None


new_linked_list = LinkedList()
new_linked_list.make_new_list()

new_linked_list.delete_at_start()
new_linked_list.delete_at_end()
new_linked_list.traverse_list()