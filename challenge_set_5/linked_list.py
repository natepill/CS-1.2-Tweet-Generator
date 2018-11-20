class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_end(self):
        current_node = self.head
        while current_node.next is not None:
            print("{ TRAVERSED }")
            previous_node = current_node
            current_node = current_node.next
        print(previous_node.data)
        previous_node.next = None
        print(previous_node.next)
        print("----------")

    def delete_node(self, node):
        current_node = self.head

        while True:
            if node is self.head:
                self.head = node.next
                del node
                break

            previous_node = current_node
            if current_node.next is node:
                next_node = node.next
                previous_node.next = next_node
                node.next = None
                break

            if current_node.next is None:
                # raise ValueError('Item not found: {}'.format(node.data))
                print(('Item not found: {}'.format(node.data)))
                break

            current_node = current_node.next




    def list_length(self, node):
        counter = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            counter += 1
        return counter

    def insert_end(self, newNode):

        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def insert_at(self, new_node, position):

        if position == 0:
            self.insertHead(new_node)
            return

        if position < 0 or position > self.list_length(self.head):
            print("Invalid position")
            return

        current_node = self.head
        current_position = 0
        while True:
            if current_position ==  position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

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

    def insert_head(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        del temp




node = Node("John")
node2 = Node("Jen")
node3 = Node("LOL")
node4 = Node("Inserted At")
node5 = Node("Hello!")



linkedlist = LinkedList()
linkedlist.insert_end(node)
linkedlist.insert_end(node2)
linkedlist.insert_end(node3)
linkedlist.insert_end(node5)


# linkedlist.display_list()
# linkedlist.insert_head("New Head") #creates a node with the value of "NewHead" as a value
linkedlist.insert_at(node4, 2)
# linkedlist.display_list()
# print(linkedlist.list_length(node3))
# linkedlist.display_list()
print("-----------")
# linkedlist.delete_node(node3)
# linkedlist.delete_node(node2)
# linkedlist.delete_node(node)
linkedlist.delete_node(node)
# linkedlist.display_list()

# print(linkedlist.list_length(node3))


anotherLinkedList = LinkedList()
another_node = Node("Head Node")
another_node2 = Node("Mid Node")
another_node3 = Node("Tail Node")
anotherLinkedList.insert_end(another_node)
anotherLinkedList.insert_end(another_node2)
anotherLinkedList.insert_end(another_node3)

anotherLinkedList.display_list()
anotherLinkedList.delete_node(node)
