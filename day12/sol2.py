from queue import Queue

maps = []

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())
    
m = len(maps)
n = len(maps[0])
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]

cl = [[0 for _ in range(n)] for _ in range(m)]


def bfs(u, v):
    area = 1
    perimeter = 4
    cl[u][v] = 1
    q = Queue()
    plots = []
    q.put((u, v))
    plots.append((u, v))
    while not q.empty():
        (i, j) = q.get()
        for t in range(4):
            x = i + tx[t]
            y = j + ty[t]
            if (x >= 0 and x < m and y >= 0 and y < n):
                if maps[x][y] == maps[u][v]:
                    perimeter -= 1
                    if cl[x][y] == 0:
                        area += 1
                        perimeter += 4
                        q.put((x, y))
                        plots.append((x, y))
                        cl[x][y] = 1
    total = 0
    for plot in plots:
        (i, j) = plot
        for t in range(4):
            x = i + tx[t]
            y = j + ty[t]
            if (x >= 0 and x < m and y >= 0 and y < n):
                if maps[x][y] == maps[u][v]:
                    if t == 1 or t == 3:
                        if (x >= 1 and maps[i-1][j] != maps[u][v] and maps[x-1][y] != maps[u][v]) or x == 0:
                            total += 1
                        if (x < m - 1 and maps[i+1][j] != maps[u][v] and maps[x+1][y] != maps[u][v]) or x == m-1:
                            total += 1
                    if t == 0 or t == 2:
                        if (y >= 1 and maps[i][j-1] != maps[u][v] and maps[x][y-1] != maps[u][v]) or y == 0:
                            total += 1
                        if (y < n - 1 and maps[i][j+1] != maps[u][v] and maps[x][y+1] != maps[u][v]) or y == n-1:
                            total += 1
    total //= 2
    perimeter -= total
    return area * perimeter
    
result = 0

for i in range(m):
    for j in range(n):
        if cl[i][j] == 0:
            result += bfs(i, j)
print(result)
print(m)
print(n)