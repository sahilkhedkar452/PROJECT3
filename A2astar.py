import heapq

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Priority queue
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Track costs
    g_cost = {start: 0}
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current

        # 4 directions
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost

                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_cost, (nx, ny)))

                    parent[(nx, ny)] = current

    return None


# ----------- MAIN ------------

# 0 = free, 1 = blocked
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = a_star(grid, start, goal)

print("Path found:", path)