from queue import Queue

maps = []

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())
    
m = len(maps)
n = len(maps[0])
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]

visit = set()
for i in range(m):
    for j in range(n):
        if maps[i][j] == '^':
            x = i
            y = j
            direction = 0
            visit.add((i, j))
            while True:
                u = x + tx[direction]
                v = y + ty[direction]
                if u >= 0 and u < m and v >= 0 and v < n:
                    if maps[u][v] == '#':
                        direction = (direction + 1) % 4
                    else:
                        x = u
                        y = v 
                        visit.add((x, y))
                else:
                    break

print(len(visit))