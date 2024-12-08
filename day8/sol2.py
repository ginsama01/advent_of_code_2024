
maps = []
antenna = {}

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())

m = len(maps)
n = len(maps[0])

for i in range(m):
    for j in range(n):
        if maps[i][j] != '.':
            if maps[i][j] in antenna:
                antenna[maps[i][j]].append((i, j))
            else:
                antenna[maps[i][j]] = [(i, j)]

antinode = set()

for frequency in antenna:
    t = len(antenna[frequency])
    for i in range(t-1):
        for j in range(i + 1, t, 1):
            (x1, y1) = antenna[frequency][i]
            (x2, y2) = antenna[frequency][j]
            antinode.add((x1, y1))
            antinode.add((x2, y2))
            (tx, ty) = (x2 - x1, y2 - y1)
            (u, v) = (x1 + tx, y1 + ty)
            while u >= 0 and u < m and v >= 0 and v < n:
                antinode.add((u, v))
                (u, v) = (u + tx, v + ty)
            (u, v) = (x1 - tx, y1 - ty)
            while u >= 0 and u < m and v >= 0 and v < n:
                antinode.add((u, v))
                (u, v) = (u - tx, v - ty)

print(len(antinode))