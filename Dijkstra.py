n = int(input("Enter number of vertices: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 0:
            row[j] = 999

    cost.append(row)

source = int(input("Enter source vertex: "))

distance = cost[source][:]
visited = [0] * n

distance[source] = 0
visited[source] = 1

# Dijkstra Algorithm
for _ in range(n - 1):

    minimum = 999
    next_node = -1

    for i in range(n):
        if not visited[i] and distance[i] < minimum:
            minimum = distance[i]
            next_node = i

    visited[next_node] = 1

    for i in range(n):
        if (not visited[i] and
            minimum + cost[next_node][i] < distance[i]):

            distance[i] = minimum + cost[next_node][i]

print("Shortest Distance:")

for i in range(n):
    print(source, "->", i, "=", distance[i])
