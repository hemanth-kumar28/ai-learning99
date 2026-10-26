import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        h, g, node, path = heapq.heappop(pq)

        if g > best_cost.get(node, float('inf')):
            continue
        print(node, end=" ")
        if(goal==node):
            print("found!")
            print("-> ".join(path))
            print("cost: ",g)
            return

        for neighbor, weight in graph[node]:
            new_cost = g + weight
            if(new_cost < best_cost.get(neighbor, float('inf'))):
                best_cost[neighbor] = new_cost
                new_h = heuristic[neighbor]+ new_cost
                heapq.heappush(
                    pq, 
                    (new_h, new_cost, neighbor, path + [neighbor])
                )

    print("not found")
    
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 5)],
    'G': []
}

heuristic = {
    'A':6, 'B':5, 'C':8, 'D':4, 'E':3, 'F':5, 'G':0
}

astar(graph, heuristic, 'A','G')