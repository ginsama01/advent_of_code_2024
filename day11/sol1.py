
nums = []

with open ("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip().split()))

for t in range(10):
    new_nums = []
    for num in nums:
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
    nums = new_nums
    print(len(nums))

print(nums)