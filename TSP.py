from itertools import permutations

def tsp():
    cities = ['B','C','D']
    dist = {
    'A': {'B': 10, 'C': 16, 'D': 20},
    'B': {'A': 10, 'C': 18, 'D': 12},
    'C': {'A': 16, 'B': 18, 'D': 14},
    'D': {'A': 20, 'B': 12, 'C': 14}
    }
    
    best_cost = float('inf')
    best_tour = []

    for order in permutations(cities):
        tour = ['A'] + list(order) + ['A']
        cost = 0
        for i in range(len(tour) - 1):
            cost+= dist[tour[i]][tour[i+1]]

        print(" -> ".join(tour) , "| Cost: " , cost)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
        

    print("minimum")
    print(" -> ".join(best_tour) , "| Cost: " , best_cost)
    
tsp()
