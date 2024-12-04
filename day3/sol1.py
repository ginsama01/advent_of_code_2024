result = 0

with open ("input.txt", "r") as file:
    for line in file:
        positions = []
        start = 0
        while True:
            index = line.find("mul(", start)
            if index == -1:
                break
            positions.append(index)
            start = index + 1
        
        for position in positions:
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
                result += int(nums[0]) * int(nums[1])

print(result)