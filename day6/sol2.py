# Bad solution

from queue import Queue

maps = []

with open ("input.txt", "r") as file:
    for line in file:
        maps.append(line.strip())
    
m = len(maps)
n = len(maps[0])
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]

result = 0

for i in range(m):
    for j in range(n):
        if maps[i][j] == '^':
            st_x = i
            st_y = j

for i in range(m):
    for j in range(n):
        if maps[i][j] == '.':
            x = st_x
            y = st_y
            maps[i] = maps[i][:j] + '#' + maps[i][j+1:]
            direction = 0
            color = {}
            color[(x, y, direction)] = 1
            while True:
                u = x + tx[direction]
                v = y + ty[direction]
                if u >= 0 and u < m and v >= 0 and v < n:
                    if maps[u][v] == '#':
                        direction = (direction + 1) % 4
                    else:
                        x = u
                        y = v 

                    if (x, y, direction) in color:
                        result += 1
                        break
                    
                    color[(x, y, direction)] = 1
                else:
                    break
            
            maps[i] = maps[i][:j] + '.' + maps[i][j+1:]


print(result)