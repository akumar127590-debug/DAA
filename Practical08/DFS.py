n = int(input("Vertices: "))
g = {}

for i in range(n):
    v = input("Vertex: ")
    g[v] = input("Adjacent: ").split()

s = input("Start: ")
vis = set()

def dfs(v):
    vis.add(v)
    print(v, end=" ")
    for x in g[v]:
        if x not in vis:
            dfs(x)

dfs(s)
