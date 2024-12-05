
data = {}
result = 0

with open ("input.txt", "r") as file:
    for line in file:
        if "|" in line:
            nums = line.strip().split("|")
            if nums[1] in data:
                data[nums[1]].append(nums[0])
            else:
                data[nums[1]] = [nums[0]]
        elif "," in line:
            nums = line.strip().split(",")
            deny_set = set()
            ok = True
            for num in nums:
                if num in deny_set:
                    ok = False
                    break
                if num in data:
                    deny_set.update(data[num])
            if ok:
                print(nums)
                result += int(nums[len(nums) // 2])

print(result)


