maps = []
reachable = {}
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]
m = 0
n = 0

def calculate(i, j):
    if maps[i][j] == '9':
        if (i, j) not in reachable:
            reachable[(i, j)] = set()
            reachable[(i, j)].add((i, j))
        return
    if (i, j) in reachable:
        return
    reachable[(i, j)] = set()
    for t in range(4):
        u = i + tx[t]
        v = j + ty[t]
        if u < 0 or u >= m or v < 0 or v >= n:
            continue
        if maps[u][v] != '.' and int(maps[u][v]) == int(maps[i][j]) + 1:
            calculate(u, v)
            reachable[(i, j)].update(reachable[(u, v)])
    return

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())
    
m = len(maps)
n = len(maps[0])

result = 0
for i in range(m):
    for j in range(n):
        if maps[i][j] == '0':
            calculate(i, j)
            result += len(reachable[(i, j)])

print(result)
