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

    def insert_in_emptylist(self, data):
        if self.start_node is not None:
            print("List is not empty")
            return
        else:
            new_node = Node(data)
            self.start_node = new_node

    def insert_in_list(self):
        if self.start_node is not None:
            print("List is not empty")
            return
        else:
            num = int(input("enter data: "))
            new_node.item = num
            self.start_node = new_node

    def insert_at_begin(self, data):
        if self.start_node is None:
            print("no element in LL :")
            return
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            print("no element is there in LL :")
            return
        new_node = Node(data)
        ptr = self.start_node
        while ptr.ref is not None:
            ptr = ptr.ref
        ptr.ref = new_node

    def insert_before(self, x, data):
        if self.start_node is None:
            print("no element in LL :")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        ptr = self.start_node

        while ptr.ref is not None:
            if ptr.ref.item == x:
                break
            ptr = ptr.ref

        if ptr.ref is None:
            print("the searched item is not in LL :")
            return
        else:
            new_node = Node(data)
            new_node.ref = ptr.ref
            ptr.ref = new_node


L1 = LinkedList()
L1.insert_in_emptylist(15)
L1.insert_at_begin(80)
L1.insert_at_end(50)
L1.insert_before(50, 10)
L1.traverse_list()
