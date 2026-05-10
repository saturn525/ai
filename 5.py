n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n

# Check safe color
def is_safe(node, c):

    for i in range(n):

        if graph[node][i] == 1 and color[i] == c:
            return False

    return True


# Solve graph coloring
def solve(node):

    if node == n:

        print("Solution:")

        for i in range(n):
            print("Vertex", i,
                  "-> Color", color[i])
        return

    for c in range(1, m + 1):

        if is_safe(node, c):

            color[node] = c
            solve(node + 1)

            color[node] = 0


solve(0)
