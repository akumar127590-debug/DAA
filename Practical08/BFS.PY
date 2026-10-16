n = int(input("Vertices: "))
g = {}

for i in range(n):
    v = input("Vertex: ")
    g[v] = input("Adjacent: ").split()

s = input("Start: ")
vis = {s}
q = [s]

while q:
    v = q.pop(0)
    print(v, end=" ")
    for x in g[v]:
        if x not in vis:
            vis.add(x)
            q.append(x)
