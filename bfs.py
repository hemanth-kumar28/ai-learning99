from collections import deque
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()

    while(True):
        node = queue.popleft()

        if(node not in visited):
            print(node ,end = " ")
            if(node == goal):
                return        

            visited.add(node)
        
        for neighbhor in graph[node]:
            if(neighbhor not in visited):
                queue.append(neighbhor)
        
    print("goal not found")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
        
bfs(graph, 'A','F')