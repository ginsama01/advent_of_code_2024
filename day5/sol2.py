
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
            if ok == False:
                for i in range(len(nums)-1, -1, -1):
                    for j in range(1, i+1, 1):
                        if nums[j-1] in data and nums[j] in data[nums[j-1]]:
                            nums[j-1], nums[j] = nums[j], nums[j-1]
                result += int(nums[len(nums) // 2])



print(result)


