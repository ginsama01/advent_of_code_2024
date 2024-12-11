from functools import cache

@cache
def recursive(num, m):
    if m == 0:
        return 1
    new_nums = []
    if num == 0:
        new_nums.append(1)
    elif len(str(num)) % 2 == 0:
        n = len(str(num)) // 2
        num1 = str(num)[:n]
        num2 = str(num)[n:]
        new_nums.append(int(num1))
        new_nums.append(int(num2))
    else:
        new_nums.append(num*2024)    
    return sum(recursive(x, m - 1) for x in new_nums)

nums = []

with open ("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip().split()))

result = sum(recursive(x, 75) for x in nums)
print(result)