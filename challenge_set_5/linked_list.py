class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):

        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def insertAt(self, node, position):

    def display_list(self):

        if self.head == None:
            print("List is empty")
            return

        current_node = self.head

        while True:
            if current_node.next is None:
                print(current_node.data)
                break

            print(current_node.data)
            current_node = current_node.next

    def insertHead(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        del temp




node = Node("John")
node2 = Node("Jen")
node3 = Node("LOL")

linkedlist = LinkedList()
linkedlist.insertEnd(node)
linkedlist.insertEnd(node2)
linkedlist.insertEnd(node3)
# linkedlist.display_list()
linkedlist.insertHead("NewHead")
linkedlist.display_list()
