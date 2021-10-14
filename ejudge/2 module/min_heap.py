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

    class __HeapNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        @staticmethod
        def get_parent_index(index_):
            return (index_ - 1) // 2

        @staticmethod
        def get_left_child_index(index_):
            return 2 * index_ + 1

        @staticmethod
        def get_right_child_index(index_):
            return  2 * index_ + 1



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
