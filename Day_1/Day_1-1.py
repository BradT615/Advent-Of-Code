with open("Day_1/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
for i in range(len(lines)):
    line = lines[i]
    val = 0
    for c in line:
        if c.isdigit():
            val = int(c) * 10
            break
    for c in line[::-1]:
        if c.isdigit():
            val += int(c)
            break
    total += val

file.close()
print(total)