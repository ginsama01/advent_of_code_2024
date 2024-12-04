
result = 0 

with open ("input1.txt", "r") as file:
    for line in file:
        fnumbers = list(map(int, line.split()))
        isSafe = 0
        for j in range(len(fnumbers)):
            numbers = fnumbers[:]
            numbers.pop(j)
            direction = 0
            if len(numbers) <= 1:
                isSafe = 1
                break
            if (numbers[0] == numbers[1] or abs(numbers[0] - numbers[1]) > 3):
                continue
            if (numbers[0] > numbers[1]):
                direction = 1
            ok = 1
            for i in range(len(numbers) - 1):
                if direction == 1:
                    if (numbers[i] <= numbers[i + 1] or numbers[i] - numbers[i + 1] > 3):
                        ok = 0
                        break
                elif direction == 0:
                    if (numbers[i] >= numbers[i + 1] or numbers[i + 1] - numbers[i] > 3):
                        ok = 0
                        break
            if ok == 1:
                isSafe = 1
                break
        if isSafe == 1:
            result += 1

print(result)
        