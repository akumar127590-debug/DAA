from itertools import permutations

n = int(input("Enter number of cities: "))
a = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    cost = sum(a[path[i]][path[i+1]] for i in range(n))
    ans = min(ans, cost)

print("Minimum Cost:", ans)
