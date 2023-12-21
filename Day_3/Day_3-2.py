with open("Day_3/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == "*":
            nums = []
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if 0 <= l < len(lines[k]) and lines[k][l].isdigit():
                        num = []
                        count = l
                        while count < len(lines[k]) and lines[k][count].isdigit():
                            num.append(lines[k][count])
                            lines[k] = lines[k][:count] + "." + lines[k][count+1:]
                            count += 1
                        count = l - 1
                        while count >= 0 and lines[k][count].isdigit():
                            num.insert(0, lines[k][count])
                            lines[k] = lines[k][:count] + "." + lines[k][count+1:]
                            count -= 1
                        num = int("".join(num))
                        nums.append(num)
            if len(nums) == 2:
                total += nums[0] * nums[1]

print(total)
file.close()