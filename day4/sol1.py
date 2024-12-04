import queue

matrices = []

with open ("input.txt", "r") as file:
    for line in file:
        matrices.append(line.strip())



tx = [-1, -1, -1, 0, 0, 1, 1, 1]
ty = [-1, 0, 1, 1, -1, -1, 0, 1]
ts = ['M', 'A', 'S']

m = len(matrices)
n = len(matrices[0])
result = 0
for i in range(m):
    for j in range(n):
        if matrices[i][j] == 'X':
            for t in range(8):
                ok = True
                for c in range(3):
                    u = i + tx[t] * (c+1)
                    v = j + ty[t] * (c+1)
                    # print(matrices[u][v])
                    if u >= 0 and u < m and v >= 0 and v < n and matrices[u][v] == ts[c]:
                        # print(matrices[u][v])
                        continue
                    else:
                        ok = False
                        break
                if ok:
                    result += 1

print(result)