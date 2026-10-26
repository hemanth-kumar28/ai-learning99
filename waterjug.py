import heapq

def heuristic(x,y):
    return min(abs(x-2),abs(y-2))

def waterjug():
    start = (0,0)
    goal = None

    pq = [(heuristic(*start), 0, start, [start])]
    best_cost = {start : 0}

    while pq:
        h, g, (x,y), path = heapq.heappop(pq)

        if g > best_cost.get((x,y), float('inf')):
            continue
        
        if(x==2 or y==2):
            print("found!")
            for state in path:
                print(state)
            print("cost: ",g)
            return
        
        a = (4,3) #x cap = 4, y cap = 3
        next_states = [
            (4, y), #fill x
            (x, 3), #fill y
            (0, y), #empty x
            (x, 0), #empty y
            (x - min(x, 3-y), y + min(x, 3-y)), #pour x to y
            (x + min(y, 4-x), y - min(y, 4-x))  #pour y to x
        ]

        for state in next_states:
            nx,ny = state

            new_cost = g + 1
            if new_cost < best_cost.get((nx,ny), float('inf')):
                best_cost[(nx,ny)] = new_cost #DONT forgte to UPDATE BEST_COST
                new_h = new_cost + heuristic(nx,ny)

                heapq.heappush(pq,
                    (new_h, new_cost, (nx,ny), path + [(nx,ny)])
                )
    print("not found")

waterjug()

