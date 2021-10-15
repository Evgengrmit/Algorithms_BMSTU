import re
import sys


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
            return 2 * index_ + 1

    # Восстановление свойств кучи
    @staticmethod
    def __sift_up(indexes_, array_, idx_):
        """
        Просеиваем вверх
        """
        if idx_ != 0:
            parent_idx = MinHeap.__HeapVertex.get_parent_index(idx_)
            if array_[idx_].key < array_[parent_idx].key:
                indexes_[array_[idx_].key] = parent_idx
                indexes_[array_[parent_idx].key] = idx_
                array_[idx_], array_[parent_idx] = array_[parent_idx], array_[idx_]
                MinHeap.__sift_up(indexes_, array_, parent_idx)

    @staticmethod
    def __sift_down(indexes_, array_, idx_):
        """
        Просеиваем вниз
        """
        smallest_idx = idx_
        left_child_idx = MinHeap.__HeapVertex.get_left_child_index(idx_)
        right_child_idx = MinHeap.__HeapVertex.get_right_child_index(idx_)
        if left_child_idx < len(array_) and array_[left_child_idx].key < array_[smallest_idx].key:
            smallest_idx = left_child_idx

        if right_child_idx < len(array_) and array_[right_child_idx].key < array_[smallest_idx].key:
            smallest_idx = right_child_idx

        if smallest_idx != idx_:
            indexes_[array_[idx_].key] = smallest_idx
            indexes_[array_[smallest_idx].key] = idx_
            array_[idx_], array_[smallest_idx] = array_[smallest_idx], array_[idx_]
            MinHeap.__sift_down(indexes_, array_, idx_)

    def add(self, key_=None, value_=None):
        if key_ is None or value_ is None:
            raise MinHeapException('error')
        if not self.__array:
            self.__array.append(MinHeap.__HeapVertex(key_, value_))
            self.__indexes[key_] = 0
            return
        if key_ in self.__indexes:
            raise MinHeapException('error')
        self.__array.append(MinHeap.__HeapVertex(key_, value_))
        self.__indexes[key_] = len(self.__array) - 1
        MinHeap.__sift_up(self.__indexes, self.__array, len(self.__array) - 1)

    def set(self, key_=None, value_=None):
        if key_ is None or value_ is None or key_ not in self.__indexes:
            raise MinHeapException('error')
        self.__array[self.__indexes[key_]] = value_

    def delete(self, key_=None):
        if not self.__array or key_ is None or key_ not in self.__indexes:
            raise MinHeapException('error')
        number_of_vertexes = len(self.__array)



    def search(self, key_):
        pass

    def minimum(self):
        if not self.__array:
            raise MinHeapException('error')
        return f'{self.__array[0].key} 0 {self.__array[0].value}'

    def maximum(self):
        pass


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
    elif re.match(re.compile(r'(delete\s-?\d+$)|(search\s-?\d+$)'), line_):
        return Command(*line_.split())
    elif re.match(re.compile(r'(add\s-?\d+\s\S+$)|(set\s-?\d+\s\S+$)'), line_):
        return Command(*line_.split())

    raise MinHeapException('error')
