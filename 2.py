from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))

    visited = set()

    while not pq.empty():
        cost, node = pq.get()

        if node in visited:
            continue

        visited.add(node)

        print(node, end=" ")

        if node == goal:
            print("\nGoal reached!")
            return

        for neighbour, weight in graph[node]:
            total_cost = weight + heuristic[neighbour]
            pq.put((total_cost, neighbour))

astar('A', 'E')
