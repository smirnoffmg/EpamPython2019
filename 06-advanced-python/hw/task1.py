"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""

from collections import deque

# Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}


def somegraph(name, some_graph):
    search_deque = deque()
    print("1", search_deque)
    search_deque += some_graph[name]
    print("2", search_deque)
    storage = []
    storage.append(name)
    while search_deque:
        pop_element = search_deque.popleft()
        print("popleft search_deque", search_deque)
        print("pop element", pop_element)

        if pop_element not in storage:

            if pop_element == "Q":  # проверка условия, если True
                print(f"We are searching it in {search_deque}")
                return True
            else:
                search_deque += some_graph[pop_element]
                print("update pop element", search_deque)
                storage.append(pop_element)
        else:
            print(f"{pop_element} I am in already here", storage)
    return storage, pop_element

# somegraph("A", my_graph)
# print(somegraph("A", my_graph))


class Graph:

    def __init__(self, name, bfs_graph):
        # self.storage = [name]
        self.storage = deque(name)
        self.bfs(name, bfs_graph)
        # self.index = -1

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.index + 1 >= len(self.storage):
    #         raise StopIteration
    #     self.index = self.index + 1
    #     return self.storage[self.index]
    def __next__(self):
        if not self.storage:
            raise StopIteration
        print("next", self.storage)
        return self.storage.popleft()

    def bfs(self, name, bfs_graph):
        search_deque = deque()
        search_deque += bfs_graph[name]
        while search_deque:
            pop_element = search_deque.popleft()
            if pop_element not in self.storage:
                search_deque += bfs_graph[pop_element]
                # self.storage.append(pop_element)
                self.storage += pop_element


g1 = Graph("A", E)
for i in g1:
    print(i)






