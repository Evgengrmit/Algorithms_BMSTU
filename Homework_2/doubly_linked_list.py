class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):

        self._head = None
        self._tail = None

    def add(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def print_list(self):
        node = self._head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

    def print_list_reverse(self):
        node = self._tail
        while node:
            print(node.data, end=' ')
            node = node.prev
        print()


class Stack(DoublyLinkedList):
    def __init__(self):
        super(Stack, self).__init__()

    def push(self, data):
        super(Stack, self).add(data)

    def pop(self):
        if self._tail is None:
            raise IndexError('underflow')
        popped = self._tail.data
        if self._tail.prev is not None:
            self._tail = self._tail.prev
            self._tail.next = None
        else:
            self._head = None
            self._tail = self._tail.prev
        return popped


class Queue(DoublyLinkedList):
    def __init__(self):
        super(Queue, self).__init__()

    def push(self, data):
        super(Queue, self).add(data)

    def pop(self):
        if self._head is None:
            raise IndexError('underflow')
        popped = self._head.data
        if self._head.next is not None:
            self._head = self._head.next
            self._head.prev = None
        else:
            self._tail = None
            self._head = self._head.next
        return popped


if __name__ == '__main__':
    print('Stack:')
    my_stack = Stack()
    for i in range(3):
        my_stack.push(i)
    my_stack.print_list()
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    try:
        my_stack.pop()
    except IndexError as e:
        print(e)
    my_stack.push(5)
    my_stack.push(6)
    my_stack.print_list()

    print('Queue:')
    my_queue = Queue()
    for i in range(3):
        my_queue.push(i)
    my_queue.print_list()
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())
    try:
        my_queue.pop()
    except IndexError as e:
        print(e)
    my_queue.push(5)
    my_queue.push(6)
    my_queue.print_list()
