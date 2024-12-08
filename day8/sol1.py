
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
            (u, v) = (x1 * 2 - x2, y1 * 2 - y2)
            if (u >= 0 and u < m and v >= 0 and v < n):
                antinode.add((u, v))
            (u, v) = (x2 * 2 - x1, y2 * 2 - y1)
            if (u >= 0 and u < m and v >= 0 and v < n):
                antinode.add((u, v))

print(len(antinode))