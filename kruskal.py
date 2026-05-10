parent = [0] * 10

def find(i):
    while parent[i]:
        i = parent[i]
    return i

def union(a, b):
    parent[a] = b


n = int(input("Enter number of vertices: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 0:
            row[j] = 999

    cost.append(row)

edges = 0
min_cost = 0

print("Edges in MST:")

while edges < n - 1:

    minimum = 999
    a = b = -1

    # Find minimum edge
    for i in range(n):
        for j in range(n):
            if cost[i][j] < minimum:
                minimum = cost[i][j]
                a = i
                b = j

    u = find(a)
    v = find(b)

    # Avoid cycle
    if u != v:

        print(a, "-", b, "=", minimum)

        union(u, v)

        min_cost += minimum
        edges += 1

    cost[a][b] = cost[b][a] = 999

print("Minimum Cost =", min_cost)
