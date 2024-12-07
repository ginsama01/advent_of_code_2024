nums = []
result = 0
max_n = 0

def back_track(position, value, total):
    if position == len(nums):
        if value == total:
            return 1
        else:
            return 0
    if value > total:
        return 0
    return max(back_track(position + 1, value + nums[position], total), 
                back_track(position + 1, value * nums[position], total),
                back_track(position + 1, int(str(value) + str(nums[position])), total))

with open ("input.txt", "r") as file:
    for line in file:
        total = int(line.strip().split(":")[0])
        nums = list(map(int, line.split(":")[1].strip().split(" ")))
        max_n = max(len(nums), max_n)
        if back_track(1, nums[0], total) == 1:
            result += total

print(result)
print(max_n)
