class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def addNode(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            last_node = self.head_node
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def reverse(self):
        prev_node = None
        curr_node = self.head_node
        while curr_node.next:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head_node = curr_node
        self.head_node.next = prev_node

    def print_list(self):
        node = self.head_node
        while node:
            print(node.data, end=' ')
            node = node.next
        print()


if __name__ == '__main__':
    my_list = LinkedList()
    for i in range(100):
        my_list.addNode(i)

    my_list.print_list()
    my_list.reverse()
    my_list.print_list()
