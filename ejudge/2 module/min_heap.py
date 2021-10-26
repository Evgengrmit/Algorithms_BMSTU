import re
import sys
import math


class MinHeapException(Exception):
    pass


class MinHeap:
    def __init__(self):
        """
        В атрибуте __array хранится представление кучи в виде массива
        В атрибуте __indexes хранятся пары ключ-индекс для доступа по ключу в среднем за O(1)
        """
        self.__array = list()
        self.__indexes = dict()

    class __HeapVertex:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        @staticmethod
        def get_parent_index(index_) -> int:
            return (index_ - 1) // 2

        @staticmethod
        def get_left_child_index(index_) -> int:
            return 2 * index_ + 1

        @staticmethod
        def get_right_child_index(index_) -> int:
            return 2 * index_ + 2

    @staticmethod
    def height(array):
        return math.floor(math.log2(len(array))) + 1

    # Восстановление свойств кучи
    @staticmethod
    def __sift_up(indexes, array, idx):
        """
        Просеиваем вверх
        """
        if idx != 0:
            parent_idx = MinHeap.__HeapVertex.get_parent_index(idx)
            if array[idx].key < array[parent_idx].key:
                indexes[array[idx].key] = parent_idx
                indexes[array[parent_idx].key] = idx
                array[idx], array[parent_idx] = array[parent_idx], array[idx]
                MinHeap.__sift_up(indexes, array, parent_idx)

    @staticmethod
    def __sift_down(indexes, array, idx):
        """
        Просеиваем вниз
        """
        smallest_idx = idx
        left_child_idx = MinHeap.__HeapVertex.get_left_child_index(idx)
        right_child_idx = MinHeap.__HeapVertex.get_right_child_index(idx)
        if left_child_idx < len(array) and array[left_child_idx].key < array[smallest_idx].key:
            smallest_idx = left_child_idx

        if right_child_idx < len(array) and array[right_child_idx].key < array[smallest_idx].key:
            smallest_idx = right_child_idx

        if smallest_idx != idx:
            indexes[array[idx].key] = smallest_idx
            indexes[array[smallest_idx].key] = idx
            array[idx], array[smallest_idx] = array[smallest_idx], array[idx]
            MinHeap.__sift_down(indexes, array, smallest_idx)

    def add(self, key_to_add=None, value=None):
        if key_to_add is None or value is None or key_to_add in self.__indexes:
            raise MinHeapException('error')

        if not self.__array:
            self.__array.append(MinHeap.__HeapVertex(key_to_add, value))
            self.__indexes[key_to_add] = 0
        else:
            new_vertex = MinHeap.__HeapVertex(key_to_add, value)
            self.__array.append(new_vertex)
            self.__indexes[key_to_add] = len(self.__array) - 1
            MinHeap.__sift_up(self.__indexes, self.__array, len(self.__array) - 1)

    def set(self, key_to_set=None, value=None):
        if key_to_set is None or value is None or key_to_set not in self.__indexes:
            raise MinHeapException('error')
        i = self.__indexes[key_to_set]
        self.__array[i].value = value

    def delete(self, key_to_del=None):
        if key_to_del is None or key_to_del not in self.__indexes:
            raise MinHeapException('error')

        size = len(self.__array)
        idx = self.__indexes[key_to_del]

        if size > 1 and idx < size - 1:
            del self.__indexes[key_to_del]
            self.__indexes[self.__array[-1].key] = idx
            self.__array[idx] = self.__array[-1]
            self.__array.pop()
            parent_idx = MinHeap.__HeapVertex.get_parent_index(idx)
            if not idx or self.__array[idx].key > self.__array[parent_idx].key:
                MinHeap.__sift_down(self.__indexes, self.__array, idx)
            else:
                MinHeap.__sift_up(self.__indexes, self.__array, idx)
        else:
            del self.__indexes[key_to_del]
            self.__array.pop()

    def extract(self):
        if not self.__array:
            raise MinHeapException('error')

        first_vertex = self.__array[0]
        self.delete(first_vertex.key)
        return first_vertex.key, first_vertex.value

    def search(self, key_to_search):
        if key_to_search is None:
            raise MinHeapException('error')

        if key_to_search not in self.__indexes:
            return ()
        found_idx = self.__indexes[key_to_search]
        found_vertex = self.__array[found_idx]
        return found_idx, found_vertex.value

    def minimum(self):
        if not self.__array:
            raise MinHeapException('error')
        return self.__array[0].key, self.__array[0].value

    def maximum(self):
        if not self.__array:
            raise MinHeapException('error')

        max_vertex, max_idx = self.__array[0], 0
        number_of_vertexes = len(self.__array)

        for i in range(number_of_vertexes // 2, number_of_vertexes):
            if self.__array[i].key > max_vertex.key:
                max_vertex, max_idx = self.__array[i], i

        return max_vertex.key, max_idx, max_vertex.value

    def __print_line(self, level):
        start = 2 ** level - 1
        end = 2 ** (level + 1) - 1
        for vertex in self.__array[start:end]:
            parent_vertex = self.__array[MinHeap.__HeapVertex.get_parent_index(self.__indexes[vertex.key])]
            yield f'[{vertex.key} {vertex.value} {parent_vertex.key}]'

        if end > len(self.__array):
            for _ in range(end - len(self.__array)):
                yield '_'

    def print(self):
        if not self.__array:
            print('_')
            return
        root = self.__array[0]
        print(f'[{root.key} {root.value}]')
        height = MinHeap.height(self.__array) + 1
        for i in range(1, height - 1):
            print(' '.join(self.__print_line(i)))


class Command:
    def __init__(self, name_=None, key_=None, value_=None):
        self.name = name_
        if key_ is not None:
            self.key = int(key_)
        if value_ is not None:
            self.value = value_


def parse_command(line_):
    if re.match(re.compile(r'(min|max|print|extract)$'), line_):
        return Command(line_)
    elif re.match(re.compile(r'(delete\s-?\d+$)|(search\s-?\d+$)'), line_) \
            or re.match(re.compile(r'(add\s-?\d+\s\S+$)|(set\s-?\d+\s\S+$)'), line_):
        return Command(*line_.split())

    raise MinHeapException('error')


def main():
    my_min_heap = MinHeap()
    for line in sys.stdin:
        if line == '\n':
            continue
        try:
            line = line[:-1]
            command = parse_command(line)
            if command.name == 'add':
                my_min_heap.add(command.key, command.value)
            elif command.name == 'set':
                my_min_heap.set(command.key, command.value)
            elif command.name == 'delete':
                my_min_heap.delete(command.key)
            elif command.name == 'search':
                result = my_min_heap.search(command.key)
                if result:
                    print(f'1 {result[0]} {result[1]}')
                else:
                    print('0')
            elif command.name == 'min':
                key, value = my_min_heap.minimum()
                print(f'{key} 0 {value}')
            elif command.name == 'max':
                key, index, value = my_min_heap.maximum()
                print(f'{key} {index} {value}')
            elif command.name == 'extract':
                key, value = my_min_heap.extract()
                print(f'{key} {value}')
            elif command.name == 'print':
                my_min_heap.print()
        except MinHeapException as mhe:
            print(mhe)


if __name__ == '__main__':
    main()
