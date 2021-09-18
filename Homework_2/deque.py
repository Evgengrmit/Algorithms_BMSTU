class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):

        self._head = None
        self._tail = None

    def push_back(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def pop_back(self):
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

    def pop_front(self):
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

    def print_deque(self):
        node = self._head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

    def print_deque_reverse(self):
        node = self._tail
        while node:
            print(node.data, end=' ')
            node = node.prev
        print()


if __name__ == '__main__':
    my_deque = Deque()
    my_deque.push_back(1)
    print(my_deque.pop_front())
    my_deque.push_front(1)
    my_deque.push_back(3)
    my_deque.push_front(2)
    my_deque.push_front(4)
    my_deque.print_deque()
    my_deque.pop_back()
    my_deque.pop_front()
    my_deque.print_deque()
    my_deque.pop_back()
    my_deque.pop_front()
