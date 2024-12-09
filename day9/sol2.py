
content = ""

with open ("input.txt", "r") as file:
    content = [int(char) for char in file.read().strip()]

n = len(content)
m = n - 2 if n % 2 == 0 else n - 1
value = {}

for i in range(m, 0, -2):
    if content[i] in value:
        value[content[i]].append(i)
    else:
        value[content[i]] = [i]

sum_content = []
sum_content.append(content[0])
for i in range(1, n, 1):
    sum_content.append(sum_content[i-1] + content[i])

result = 0

def getsum(u, v):
    total = v - u + 1
    return total * (u + v) // 2


for i in range(n):
    if i % 2 == 0:
        if i == 0: 
            tmp_location = 0
        else:
            tmp_location = sum_content[i-1]
        result += i // 2 * getsum(tmp_location, tmp_location + content[i] - 1)
    else:
        tmp_location = sum_content[i-1]
        free = int(content[i])
        while free > 0:
            location = -1
            for j in range(free, 0, -1):
                if j in value:
                    if len(value[j]) > 0:
                        if value[j][0] < i:
                            del value[j]
                        else:
                            location = max(location, value[j][0])
            if location == -1:
                break
            num = content[location]
            result += location // 2 * getsum(tmp_location, tmp_location + num - 1)
            tmp_location = tmp_location + num
            free -= num
            del value[content[location]][0]
            content[location] = 0
            

print(result)

