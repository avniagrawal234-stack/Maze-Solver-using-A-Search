import heapq
maze = [
    ['S','.','.','#','.'],
    ['#','#','.','#','.'],
    ['.','.','.','.','.'],
    ['.','#','#','#','.'],
    ['.','.','.','G','.']
]

ROWS = len(maze)
COLS = len(maze[0])

for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == 'S':
            start = (i,j)
        elif maze[i][j] == 'G':
            goal = (i,j)
            
            
def heuristic(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    came_from = {}
    
    g_cost = {start: 0}
    while priority_queue:
        current = heapq.heappop(priority_queue)[1]
        
        if current == goal:
            path = []
            
            while current in came_from:
                path.append(current)
                current = came_from[current]
                
            path.append(start)
            path.reverse()
            
            return path
    row,col = current
    
    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1),
    ]
    
    for dr , dc in directions:
        
        nr = row + dr
        nc = col + dc
        
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            
            if maze[nr][nc] == '#':
                continue
            
            neighbor = (nr, nc)
            new_cost = g_cost[current] + 1
            
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                
                g_cost[neighbor] = new_cost
                f = new_cost + heuristic(neighbor, goal)
                
                heapq.heappush(priority_queue, (f, neighbor))
                came_from[neighbor]= current
                
    return None

path = astar(start, goal)

if path:
    print("Shortest Path Found!\n")
    
    for r, c in path:
        
        if maze[r][c] not in ['S', 'G']:
            maze[r][c] = '*'
            
    for row in maze:
        print(" ".join(row))
        
    print("\nPath Coordianted:")
    print(path)
    
else:
    print("Goal is unreachable.")