
list1 = []
list2 = []

for i in range(100000):
    list2.append(0)

with open ("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2[num2] += 1


total = 0
for i in range(len(list1)):
    total += list1[i] * list2[list1[i]]

print(total)
