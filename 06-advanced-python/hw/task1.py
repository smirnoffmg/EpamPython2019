"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""


class Graph:
    def __init__(self, E):
        self._E = E

    def __getitem__(self, name):
        return self._E[name]

    def __iter__(self):
        return iter(self._E)

    def keys(self):
        return self._E.keys()

    def values(self):
        return self._E.values()

    def items(self):
        return self._E.items()


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)



