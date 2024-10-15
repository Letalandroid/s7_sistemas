import random
import heapq

# Función para generar un laberinto aleatorio usando el algoritmo de división recursiva
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def carve_passages(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                maze[ny][nx] = 0
                carve_passages(nx, ny)
    
    start_x, start_y = 0, 0
    maze[start_y][start_x] = 0
    carve_passages(start_x, start_y)
    
    return maze

# Algoritmo A* para encontrar el camino más corto en el laberinto
def a_star(maze, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distancia Manhattan

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[1]][neighbor[0]] == 0:
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []

# Función para imprimir el laberinto
def print_maze(maze):
    for row in maze:
        print("".join(['#' if cell == 1 else '.' for cell in row]))

# Genera un laberinto de tamaño 21x21
width, height = 21, 21
maze = generate_maze(width, height)

# Define el punto de inicio y el objetivo
start = (0, 0)
goal = (width - 1, height - 1)

# Imprime el laberinto
print("Laberinto generado:")
print_maze(maze)

# Aplica A* para encontrar el camino más corto
path = a_star(maze, start, goal)

# Imprime el laberinto con el camino encontrado
print("\nCamino encontrado:")
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if (x, y) == start:
            print("S", end="")
        elif (x, y) == goal:
            print("G", end="")
        elif (x, y) in path:
            print("*", end="")
        else:
            print("#" if cell == 1 else ".", end="")
    print()