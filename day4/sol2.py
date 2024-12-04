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
        if matrices[i][j] == 'A':
            if i >= 1 and j >= 1 and i < m - 1 and j < n - 1:
                s1 = matrices[i-1][j-1] + matrices[i][j] + matrices[i+1][j+1]
                s2 = matrices[i-1][j+1] + matrices[i][j] + matrices[i+1][j-1]
                if (s1 == 'MAS' or s1 == 'SAM'):
                    if (s2 == 'MAS' or s2 == 'SAM'):
                        result += 1
        
print(result)