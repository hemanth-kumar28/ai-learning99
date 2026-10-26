def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while(True):
        node = stack.pop()

        if node not in visited:
            
            print(node, end = " ")

            if node == goal:
                return 
            
            visited.add(node)
        
        for neighbhor in reversed(graph[node]):
            if neighbhor not in visited:
                stack.append(neighbhor)
        
    print("goal node not found!")

    
graph = {

    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []

}

dfs(graph,'A', 'F')
