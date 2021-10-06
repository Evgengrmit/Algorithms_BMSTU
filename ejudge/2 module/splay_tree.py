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

        def remove_children(self):
            if self.has_right_child():
                self.right_child = None

            if self.has_left_child():
                self.left_child = None

        def is_left_child(self):
            return self.parent.left_child == self

        def __str__(self):
            if self.parent is None:
                return f'[{self.key} {self.value}]'
            else:
                return f'[{self.key} {self.value} {self.parent.key}]'

    def __init__(self):
        self.__root = None

    def __right_rotation(self, x=__SplayNode()):
        y = x.left

        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:  # узел node_x - корень
            self.__root = y
        elif x == x.parent.right:  # узел node_x - правый ребенок
            x.parent.right = y
        else:  # узел node_x - левый ребенок
            x.parent.left = y

        y.right = x
        x.parent = y

    def __left_rotation(self, x=__SplayNode()):
        y = x.right

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:  # узел node_x - корень
            self.__root = y
        elif x == x.parent.left:  # узел node_x - левый ребенок
            x.parent.left = y
        else:  # узел node_x - правый ребенок
            x.parent.right = y

        y.left = x
        x.parent = y

    def __zig(self, node):


    def __splay(self, node=__SplayNode()):
        if node is None:
            return
        while node.has_parent():
            if node.parent == self.__root:  # узел - ребенок корня
                if node.is_left_child():
                    self.__right_rotation(node.parent)
                else:
                    self.__left_rotation(node.parent)
            else:
