import re
import sys
from collections import deque

sys.setrecursionlimit(10600000)


class SplayTreeException(Exception):
    pass


class SplayTree:
    class __SplayNode:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.parent = None
            self.right_child = None
            self.left_child = None

        def has_parent(self):
            return self.parent is not None

        def has_right_child(self):
            return self.right_child is not None

        def has_left_child(self):
            return self.left_child is not None

        def is_left_child(self):
            return self.parent.left_child == self

        def is_right_child(self):
            return self.parent.right_child == self

        def __str__(self):
            if self.parent is None:
                return f'[{self.key} {self.value}]'
            else:
                return f'[{self.key} {self.value} {self.parent.key}]'

    def __init__(self):
        self.__root = None

    @staticmethod
    def depth(root):
        if root is None:
            return 0
        left_depth = SplayTree.depth(root.left_child)
        right_depth = SplayTree.depth(root.right_child)
        return max(left_depth, right_depth) + 1

    @staticmethod
    def __find(root=__SplayNode(), key=None):
        if root is None:
            return None

        if root.key == key:
            return root
        elif root.key > key and root.has_left_child():
            return SplayTree.__find(root.left_child, key)

        elif root.key < key and root.has_right_child():
            return SplayTree.__find(root.right_child, key)

        return root

    def __right_rotation(self, x=__SplayNode()):
        y = x.left_child

        x.left_child = y.right_child
        if y.has_right_child():
            y.right_child.parent = x

        y.parent = x.parent
        if x.parent is None:  # узел x - корень
            self.__root = y
        elif x.is_right_child():  # узел x - правый ребенок
            x.parent.right_child = y
        else:  # узел x - левый ребенок
            x.parent.left_child = y

        y.right_child = x
        x.parent = y

    def __left_rotation(self, x=__SplayNode()):
        y = x.right_child

        x.right_child = y.left_child
        if y.has_left_child():
            y.left_child.parent = x

        y.parent = x.parent

        if x.parent is None:  # узел x - корень
            self.__root = y
        elif x.is_left_child():  # узел x - левый ребенок
            x.parent.left_child = y
        else:  # узел x - правый ребенок
            x.parent.right_child = y

        y.left_child = x
        x.parent = y

    def __splay(self, node=__SplayNode()):
        if node is None:
            return

        while node.has_parent():

            if node.parent == self.__root:  # узел - ребенок корня
                if node.is_left_child():  # zig
                    self.__right_rotation(node.parent)
                else:  # zag
                    self.__left_rotation(node.parent)
            else:
                parent = node.parent  # родитель
                grand_parent = node.parent.parent  # дед

                if node.is_left_child() and parent.is_left_child():  # zig_zig
                    self.__right_rotation(grand_parent)
                    self.__right_rotation(parent)

                elif node.is_right_child() and parent.is_right_child():  # zag_zag
                    self.__left_rotation(grand_parent)
                    self.__left_rotation(parent)

                elif node.is_left_child() and parent.is_right_child():  # zig_zag
                    self.__right_rotation(parent)
                    self.__left_rotation(grand_parent)
                elif node.is_right_child() and parent.is_left_child():  # zag_zig
                    self.__left_rotation(parent)
                    self.__right_rotation(grand_parent)

    def add(self, key=None, value=None):
        if key is None or value is None:
            raise SplayTreeException('error')

        parent_node = SplayTree.__find(self.__root, key)

        if parent_node is None:
            self.__root = self.__SplayNode(key, value)
            return

        if parent_node.key == key:
            self.__splay(parent_node)
            raise SplayTreeException('error')
        elif parent_node.key > key:
            added_node = parent_node.left_child = self.__SplayNode(key, value)
        else:
            added_node = parent_node.right_child = self.__SplayNode(key, value)

        added_node.parent = parent_node
        self.__splay(added_node)

    def search(self, key):
        if key is None:
            raise SplayTreeException('error')

        searched_node = SplayTree.__find(self.__root, key)
        self.__splay(searched_node)

        if not searched_node or searched_node.key != key:
            return '0'

        return f'1 {self.__root.value}'

    def set(self, key, value):
        if key is None or value is None:
            raise SplayTreeException('error')

        set_node = SplayTree.__find(self.__root, key)
        self.__splay(set_node)
        if set_node is None or set_node.key != key:
            raise SplayTreeException('error')

        self.__root.value = value

    @staticmethod
    def __max(root):
        temp_node = root
        while temp_node.right_child is not None:
            temp_node = temp_node.right_child
        return temp_node

    def maximum(self):
        if self.__root is None:
            raise SplayTreeException('error')
        max_node = SplayTree.__max(self.__root)
        self.__splay(max_node)
        return f'{max_node.key} {max_node.value}'

    @staticmethod
    def __min(root):
        temp_node = root
        while temp_node.left_child is not None:
            temp_node = temp_node.left_child
        return temp_node

    def minimum(self):
        if self.__root is None:
            raise SplayTreeException('error')

        min_node = SplayTree.__min(self.__root)
        self.__splay(min_node)
        return f'{min_node.key} {min_node.value}'

    def delete(self, key):
        if key is None:
            raise SplayTreeException('error')

        del_node = SplayTree.__find(self.__root, key)
        self.__splay(del_node)

        if del_node is None or del_node.key != key:
            raise SplayTreeException('error')

        if not del_node.has_left_child() and not del_node.has_right_child():
            self.__root = None
        elif not del_node.has_left_child():
            self.__root = del_node.right_child
            self.__root.parent = None
        elif not del_node.has_right_child():
            self.__root = del_node.left_child
            self.__root.parent = None
        else:
            new_root = SplayTree.__max(del_node.left_child)
            self.__splay(new_root)
            new_root.right_child = del_node.right_child
            if new_root.has_right_child():
                new_root.right_child.parent = new_root

    @staticmethod
    def __print_node(node_):
        return str(node_) if node_ is not None else '_'

    @staticmethod
    def __print_line(q_, n_, d_):
        d_ -= 1  # чтобы на последней итерации просто выводить и не засорять deque
        for i in range(len(q_)):
            if n_ < d_:
                curr_node = q_.popleft()
                if not curr_node:
                    q_.append(None)
                    q_.append(None)
                else:
                    q_.append(curr_node.left_child)
                    q_.append(curr_node.right_child)
                yield SplayTree.__print_node(curr_node)
            else:
                yield SplayTree.__print_node(q_.popleft())

    def print(self):
        depth = SplayTree.depth(self.__root)
        if depth == 0:
            print('_')
            return
        queue = deque()
        queue.append(self.__root)
        for number_of_layer in range(depth):
            print(' '.join(SplayTree.__print_line(queue, number_of_layer, depth)))


class Command:
    def __init__(self, name_=None, key_=None, value_=None):
        self.name = name_
        if key_ is not None:
            self.key = int(key_)
        if value_ is not None:
            self.value = value_


def parse_command(line_):
    if re.match(re.compile(r'(min|max|print)$'), line_):
        return Command(line_)
    elif re.match(re.compile(r'(delete\s-?\d+$)|(search\s-?\d+$)'), line_) or re.match(
            re.compile(r'(add\s-?\d+\s\S+$)|(set\s-?\d+\s\S+$)'), line_):
        return Command(*line_.split())

    raise SplayTreeException('error')


def main():
    my_splay_tree = SplayTree()
    for line in sys.stdin:
        if line == '\n':
            continue
        try:
            line = line[:-1]
            command = parse_command(line)
            if command.name == 'add':
                my_splay_tree.add(command.key, command.value)
            elif command.name == 'set':
                my_splay_tree.set(command.key, command.value)
            elif command.name == 'delete':
                my_splay_tree.delete(command.key)
            elif command.name == 'search':
                print(my_splay_tree.search(command.key))
            elif command.name == 'min':
                print(my_splay_tree.minimum())
            elif command.name == 'max':
                print(my_splay_tree.maximum())
            elif command.name == 'print':
                my_splay_tree.print()
        except SplayTreeException as ste:
            print(ste)


if __name__ == '__main__':
    main()
