#Try to use recursive with memory
maps = []
l = []
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]
m = 0
n = 0

def calculate(i, j):
    if maps[i][j] == '9':
        return 1
    if l[i][j] != -1:
        return l[i][j]
    l[i][j] = 0
    for t in range(4):
        u = i + tx[t]
        v = j + ty[t]
        if u < 0 or u >= m or v < 0 or v >= n:
            continue
        if maps[u][v] != '.' and int(maps[u][v]) == int(maps[i][j]) + 1:
            l[i][j] += calculate(u, v)
    return l[i][j]

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())
    
m = len(maps)
n = len(maps[0])

l = [[-1 for _ in range(n)] for _ in range(m)]

result = 0
for i in range(m):
    for j in range(n):
        if maps[i][j] == '0':
            result += calculate(i, j)

print(result)
