import sys
from collections import deque
import re


class VertexStatus:
    def __init__(self, col=False, neighb=None):
        if neighb is None:
            neighb = []
        self.colour = col
        self.neighbours = neighb


class Graph:
    def __init__(self):
        self.list_of_adjacent_vertices = {}

    def add_edge(self):
        pass

    def get_graph(self):
        for value in self.list_of_adjacent_vertices.values():
            value.neighbours.sort()
        return dict(sorted(self.list_of_adjacent_vertices.items(), key=lambda x: x[0]))


class DirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge=None):
        if edge is None:
            edge = []
        if edge[0] not in self.list_of_adjacent_vertices:
            self.list_of_adjacent_vertices[edge[0]] = VertexStatus(col=False, neighb=[edge[1]])
        else:
            self.list_of_adjacent_vertices[edge[0]].neighbours.append(edge[1])
        if edge[1] not in self.list_of_adjacent_vertices:
            self.list_of_adjacent_vertices[edge[1]] = VertexStatus(col=False, neighb=[])


class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge=None):
        if edge is None:
            edge = []
        if edge[0] not in self.list_of_adjacent_vertices:
            self.list_of_adjacent_vertices[edge[0]] = VertexStatus(col=False, neighb=[edge[1]])
        else:
            self.list_of_adjacent_vertices[edge[0]].neighbours.append(edge[1])
        if edge[1] not in self.list_of_adjacent_vertices:
            self.list_of_adjacent_vertices[edge[1]] = VertexStatus(col=False, neighb=[edge[0]])
        else:
            self.list_of_adjacent_vertices[edge[1]].neighbours.append(edge[0])


def get_information(line_=''):
    if re.match(re.compile('[u d]\s\S+\s[b d]'), line_):
        return line_.split()
    else:
        raise Exception('error')


def get_edge(line_=''):
    if re.match(re.compile('\S+\s\S+'), line_):
        return line_.split()
    else:
        raise Exception('error')


def breadth_first_search(adjacent_vertices=None, first=''):
    if adjacent_vertices is None:
        adjacent_vertices = {}
    queue = deque()
    adjacent_vertices[first].colour = True
    queue.appendleft(first)
    while len(queue):
        current_vertex = queue.pop()
        print(current_vertex)
        for neighbour_vertex in adjacent_vertices[current_vertex].neighbours:
            if not adjacent_vertices[neighbour_vertex].colour:
                adjacent_vertices[neighbour_vertex].colour = True
                queue.appendleft(neighbour_vertex)


def depth_first_search_iteratively(adjacent_vertices=None, first=''):
    if adjacent_vertices is None:
        adjacent_vertices = {}
    stack = deque()
    stack.append(first)
    while len(stack):
        current_vertex = stack.pop()
        if adjacent_vertices[current_vertex].colour:
            continue
        adjacent_vertices[current_vertex].colour = True
        print(current_vertex)

        for neighbour_vertex in reversed(adjacent_vertices[current_vertex].neighbours):
            if not adjacent_vertices[neighbour_vertex].colour:
                stack.append(neighbour_vertex)


if __name__ == '__main__':
    my_graph = None
    graph_type = None
    start_vertex = None
    search_type = None
    for line in sys.stdin:
        if line == '\n':
            continue
        try:
            if line[-1] == '\n':
                line = line[:-1]
            if my_graph is None:
                graph_type, start_vertex, search_type = get_information(line)
                if graph_type == 'd':
                    my_graph = DirectedGraph()
                if graph_type == 'u':
                    my_graph = UndirectedGraph()
            else:
                my_graph.add_edge(get_edge(line))
        except Exception:
            print('')
    if search_type == 'b':
        breadth_first_search(my_graph.get_graph(), start_vertex)
    if search_type == 'd':
        depth_first_search_iteratively(my_graph.get_graph(), start_vertex)

# For recursively
# sys.setrecursionlimit(10**9)
# def depth_first_search_recursively(adjacent_vertices=None, first=''):
#     if adjacent_vertices is None:
#         adjacent_vertices = {}
#     adjacent_vertices[first].colour = True
#     print(first)
#     for neighbour_vertex in adjacent_vertices[first].neighbours:
#         if not adjacent_vertices[neighbour_vertex].colour:
#             depth_first_search_recursively(adjacent_vertices,neighbour_vertex)