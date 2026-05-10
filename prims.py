n = int(input("Enter number of vertices: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 0:
            row[j] = 999

    cost.append(row)

visited = [0] * n
visited[0] = 1

edges = 0
min_cost = 0

print("Edges in MST:")

while edges < n - 1:

    minimum = 999
    a = b = -1

    for i in range(n):
        if visited[i]:

            for j in range(n):
                if not visited[j] and cost[i][j] < minimum:
                    minimum = cost[i][j]
                    a = i
                    b = j

    print(a, "-", b, "=", minimum)

    visited[b] = 1
    min_cost += minimum
    edges += 1

print("Minimum Cost =", min_cost)
