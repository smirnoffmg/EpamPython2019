"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""

from collections import deque

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}


class Graph:

    def __init__(self, name, bfs_graph):
        self.storage = deque(name)
        self.bfs(name, bfs_graph)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.storage:
            raise StopIteration
        return self.storage.popleft()

    def bfs(self, name, bfs_graph):
        search_deque = deque()
        search_deque += bfs_graph[name]
        while search_deque:
            pop_element = search_deque.popleft()
            if pop_element not in self.storage:
                search_deque += bfs_graph[pop_element]
                self.storage += pop_element


bfs_traversal = Graph("A", E)
for i in bfs_traversal:
    print(i)






