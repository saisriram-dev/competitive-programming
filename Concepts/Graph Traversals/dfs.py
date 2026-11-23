n = 6

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n


def dfs(node):
    visited[node] = True

    print(node, end=" ")

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
