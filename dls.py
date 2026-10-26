def dls(graph, node, goal, limit):
    print(node, end=" ")

    if(node == goal):
        return True
    
    if(limit == 0):
        return False
    
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit-1): 
            return True
    
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

if(dls(graph, 'A', 'F', 2)):
    print("found!")
else: 
    print("not found!")