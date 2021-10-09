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

    def remove(self,el):
        if self._head is None or self._tail is None:
            return
        if self._head.data == el:
            if self._head.next is None:
                self._head = None
                self._tail = None
                return
            else:
                self._head.next.prev = self._head.prev
                self._head = self._head.next
                return
        curr = self._head
        while curr.next is not None:
            if curr.data == el:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            else:
                curr = curr.next
        else:
            if curr.data == el:
                # if self._tail.prev is None:
                #     self._head = None
                #     self._tail = None
                # else:
                    self._tail.prev.next = self._tail.next
                    self._tail = self._tail.prev
                    return
        raise  Exception



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

    my_list = DoublyLinkedList()
    for i in range(1):
        my_list.add(i)

    my_list.print_list()
    my_list.remove(5)
    my_list.print_list()
    print(my_list._tail.data)
