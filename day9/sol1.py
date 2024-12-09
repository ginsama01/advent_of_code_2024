
content = ""

with open ("input.txt", "r") as file:
    content = [int(char) for char in file.read().strip()]

n = len(content)
j = n - 2 if n % 2 == 0 else n - 1
result = 0
tmp_location = 0

def getsum(u, v):
    total = v - u + 1
    return total * (u + v) // 2

for i in range(n):
    if i % 2 == 0:
        result += i // 2 * getsum(tmp_location, tmp_location + content[i] - 1)
        tmp_location = tmp_location + content[i]
        if i == j:
            break
    else:
        free = int(content[i])
        while free > 0:
            num = int(content[j])
            if free < num:
                result += j // 2 * getsum(tmp_location, tmp_location + free - 1)
                tmp_location = tmp_location + free
                content[j] -= free
                free = 0
            else:
                result += j // 2 * getsum(tmp_location, tmp_location + num - 1)
                tmp_location = tmp_location + num
                free -= num
                content[j] = 0
                j -= 2

print(result)

