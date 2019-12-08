"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
import collections


class GraphIterator(collections.abc.Iterator):
    def __init__(self, E):
        self.E = E
        _iter = iter(self.E)
        self._cursor = -1
        self.start = next(_iter)
        self.bfs()

    def bfs(self):
        self.is_visited = [self.start]
        graph_deque = self.E[self.start]
        while graph_deque:
            vertex = graph_deque.pop(0)
            if vertex not in self.is_visited:
                for child in self.E[vertex]:
                    graph_deque.append(child)
                self.is_visited.append(vertex)

    def __next__(self):
        self._cursor += 1
        if self._cursor >= len(self.E):
            raise StopIteration
        return self.is_visited[self._cursor]


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self.E)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)