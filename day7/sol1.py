nums = []
result = 0

def back_track(position, value, total):
    if position == len(nums):
        if value == total:
            return 1
        else:
            return 0
    if value > total:
        return 0
    return max(back_track(position + 1, value + nums[position], total), back_track(position + 1, value * nums[position], total))

with open ("input.txt", "r") as file:
    for line in file:
        total = int(line.strip().split(":")[0])
        nums = list(map(int, line.split(":")[1].strip().split(" ")))
        if back_track(1, nums[0], total) == 1:
            result += total

print(result)

