result = 0

with open ("input.txt", "r") as file:
        line = file.read()
        positions = []
        start = 0
        while True:
            index = line.find("mul(", start)
            if index == -1:
                break
            positions.append(index)
            start = index + 1
        
        positions.sort()
        print(line.rfind("don't"))
        for i in range(len(positions)):
            position = positions[i]
            strtofind = line[0:position]
            disallow = strtofind.rfind("don't()")
            allow = strtofind.rfind("do()")
            sign = 1
            if (disallow != -1):
                sign = 0
            if (allow != -1 and allow > disallow):
                sign = 1
            s = ""
            if position + 12 <= len(line):
                s = line[position:position+12]
            else:
                s = line[position:len(line)]
            last = s.find(")", 0)
            if last == -1:
                continue
            nums = s[4:last].split(',')
            if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
                if sign == 1:
                    result += int(nums[0]) * int(nums[1])

print(result)