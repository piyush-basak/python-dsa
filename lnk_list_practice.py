class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def display_link(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


ll1 = LinkedList()
ll1.insert_at_beg(5)
ll1.insert_at_beg(7)
ll1.insert_at_beg(9)
ll1.insert_at_beg(11)
ll1.display_link()


