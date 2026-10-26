import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])] #always PUT !COST FIRST!
    best_cost = {start : 0}

    while pq:
        cost,node, path = heapq.heappop(pq)

        if cost > best_cost.get(node, float('inf')):
            continue
        
        print(node, end= " ")

        if(node == goal):
            print("found")
            print("->".join(path))
            print("cost: " ,cost)
            return
        
        for neighbor,weight in graph[node]:
            new_cost = cost + weight
            if(new_cost < best_cost.get(neighbor, float('inf'))):
                best_cost[neighbor] = new_cost
                heapq.heappush(pq,
                    ( new_cost,neighbor, path + [neighbor])
                )

    print("not found!")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 5)],
    'G': []
}

            
ucs(graph, 'A','G')