
class CityGraph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * n for i in range(n)]
        self.visited = [False] * n

    def add_graph(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def dfs(self, v):
        self.visited[v] = True
        print(v, end=' ')

        for i in range(self.n):
            if self.graph[v][i] == 1 and not self.visited[i]:
                self.dfs(i)

    def bfs(self, v):
        queue = []
        queue.append(v)
        self.visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in range(self.n):
                if self.graph[v][i] == 1 and not self.visited[i]:
                    queue.append(i)
                    self.visited[i] = True

if __name__ == '__main__':
    n = int(input("Enter the number of cities: "))
    g = CityGraph(n)

    print("Enter the edges in the graph (u v): ")
    for i in range(n):
        u, v = map(int, input().split())
        g.add_graph(u, v)

    print("Enter the starting city for traversal: ")
    v = int(input())

    print("DFS Traversal: ")
    g.dfs(v)

    g.visited = [False] * n

    print("\nBFS Traversal: ")
    g.bfs(v)

# import matplotlib.pyplot as plt

# class CityGraph:
#     def __init__(self, n):
#         self.n = n
#         self.graph = [[0] * n for i in range(n)]
#         self.visited = [False] * n

#     def add_graph(self, u, v):
#         self.graph[u][v] = 1
#         self.graph[v][u] = 1

#     def dfs(self, v):
#         self.visited[v] = True
#         print(v, end=' ')

#         for i in range(self.n):
#             if self.graph[v][i] == 1 and not self.visited[i]:
#                 self.dfs(i)

#     def bfs(self, v):
#         queue = []
#         queue.append(v)
#         self.visited[v] = True

#         while queue:
#             v = queue.pop(0)
#             print(v, end=' ')

#             for i in range(self.n):
#                 if self.graph[v][i] == 1 and not self.visited[i]:
#                     queue.append(i)
#                     self.visited[i] = True

#     def print_graph(self, coords):
#         fig, ax = plt.subplots()
#         for i in range(self.n):
#             for j in range(i, self.n):
#                 if self.graph[i][j] == 1:
#                     ax.plot([coords[i][0], coords[j][0]], [coords[i][1], coords[j][1]], 'k-', linewidth=2)

#         for i in range(self.n):
#             ax.text(coords[i][0], coords[i][1], str(i), fontsize=12, ha='center', va='center', color='w',
#                     bbox=dict(facecolor='k', edgecolor='k', boxstyle='circle'))

#         ax.set_xticks([])
#         ax.set_yticks([])
#         ax.axis('off')
#         plt.show()

# if __name__ == '__main__':
#     n = int(input("Enter the number of cities: "))
#     g = CityGraph(n)

#     print("Enter the coordinates of the cities (x y): ")
#     coords = [list(map(int, input().split())) for i in range(n)]

#     print("Enter the edges in the graph (u v): ")
#     for i in range(n):
#         u, v = map(int, input().split())
#         g.add_edge(u, v)

#     print("Enter the starting city for traversal: ")
#     v = int(input())

#     print("DFS Traversal: ")
#     g.dfs(v)

#     g.visited = [False] * n

#     print("\nBFS Traversal: ")
#     g.bfs(v)

#     print("\nGraphical Representation: ")
#     g.print_graph(coords)
