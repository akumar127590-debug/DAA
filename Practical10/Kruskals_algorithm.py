def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    edges.sort()
    cost = 0

    for w, u, v in edges:
        pu, pv = find(u), find(v)

        if pu != pv:
            parent[pu] = pv
            cost += w
            print(u, "-", v, ":", w)

    print("Minimum Cost:", cost)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

kruskal(n, edges)
