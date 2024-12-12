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
    q.put((u, v))
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
                        cl[x][y] = 1
    return area * perimeter
    
result = 0

for i in range(m):
    for j in range(n):
        if cl[i][j] == 0:
            result += bfs(i, j)
print(result)