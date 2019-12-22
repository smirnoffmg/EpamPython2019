"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
<<<<<<< HEAD
import collections


class GraphIterator(collections.abc.Iterator):
    def __init__(self, E):
        self.E = E
        self.cursor = -1
        # self.start = next(iter(self.E))
        self.is_visited = []
        for i in self.E:
            self.start = i
            if self.start not in self.is_visited:
                self.is_visited.append(self.start)
                self.bfs()
=======
>>>>>>> upsteam/master

    def bfs(self):
        graph_deque = collections.deque(self.E[self.start])
        while graph_deque:
            vertex = graph_deque.popleft()
            if vertex not in self.is_visited:
                for child in self.E[vertex]:
                    graph_deque.append(child)
                self.is_visited.append(vertex)

<<<<<<< HEAD
    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.E):
            raise StopIteration
        return self.is_visited[self.cursor]


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self.E)

=======
class Graph:
    def __init__(self, E):
        self.E = E
>>>>>>> upsteam/master

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A'], 'E': []}

<<<<<<< HEAD
graph = Graph(E)

for vertex in graph:
    print(vertex)
=======
E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
>>>>>>> upsteam/master
