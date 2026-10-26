def dls(graph, node, goal, limit):
    print(node, end=" ")

    if (node==goal):
        return True
    
    if(limit == 0):
        return False
    
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit-1):
            return True
        

def iddfs(graph, start, goal):
    for i in range(0,3):
        print()
        if dls(graph,start,goal,i):
            print(goal+ "found")
            return True

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

iddfs(graph, 'A', 'F')