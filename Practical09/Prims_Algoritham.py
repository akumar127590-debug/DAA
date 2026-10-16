
import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    total_cost = 0

    while pq:
        w, v = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True
        total_cost += w

        for neigh, e_w in graph[v]:
            if not visited[neigh]:
                heapq.heappush(pq, (e_w, neigh))

    if not all(visited):
        print("Graph is not connected!")
    else:
        print("Minimum cost =", total_cost)


n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

print("Enter edges (source destination weight):")
for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

prim(graph)
