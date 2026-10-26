def dfs():
    start = (3, 3, 1)  # (M_left, C_left, boat_side: 1=left, 0=right)
    goal = (0, 0, 0)
    visited = set()

    def is_valid(m, c):
        mr, cr = 3 - m, 3 - c
        return (0 <= m <= 3 and 0 <= c <= 3 and
                (m == 0 or m >= c) and
                (mr == 0 or mr >= cr))

    def solve(state, path):
        if state == goal:
            for s in path:
                print(s)
            return True

        visited.add(state)
        m, c, boat = state

        for dm in range(3):
            for dc in range(3):
                if 1 <= dm + dc <= 2:
                    if boat == 1:
                        nxt = (m - dm, c - dc, 0)
                    else:
                        nxt = (m + dm, c + dc, 1)

                    if is_valid(nxt[0], nxt[1]) and nxt not in visited:
                        if solve(nxt, path + [nxt]):
                            return True

        return False

    if not solve(start, [start]):
        print("No solution found")

dfs()