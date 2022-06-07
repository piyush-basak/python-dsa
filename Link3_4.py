# All kind of insertions and deletions in a singly LL by Sarasij Majumdar, Techno International Newtown

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
        n.ref = new_node;

    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

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

    def delete_after_node(self, x):  # not for deleting the first node
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        prev = n
        while prev is not None:
            if prev.item == x:
                break
            prev = n
            n = n.ref
        if n is None:
            print("item not found in the list")
        else:
            prev.ref = n.ref

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    def sort(self):
        ptr1 = self.start_node
        while ptr1.ref is not None:
            ptr2 = ptr1.ref
            while ptr2 is not None:
                if ptr1.item > ptr2.item:
                    temp = ptr1.item
                    ptr1.item = ptr2.item
                    ptr2.item = temp
                ptr2 = ptr2.ref
            ptr1 = ptr1.ref


new_linked_list = LinkedList()

new_linked_list.insert_in_emptylist(100)

new_linked_list.traverse_list()
# new_linked_list.insert_in_emptylist(100)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.make_new_list()

new_linked_list.traverse_list()

new_linked_list.delete_at_start()
new_linked_list.delete_at_end()
new_linked_list.traverse_list()

new_linked_list.delete_element_by_value(34)
new_linked_list.delete_after_node(23)
new_linked_list.traverse_list()

new_linked_list.traverse_list()

# new_linked_list.reverse_linkedlist()
# new_linked_list.traverse_list()
# new_linked_list.sort()
# new_linked_list.traverse_list()
