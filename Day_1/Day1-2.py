with open("Day_1/input.txt", "r") as file:
    lines = [line.strip() for line in file]

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0

for i in range(len(lines)):
    line = lines[i]
    val = 0
    found = False

    for c in range(len(line)):
        if line[c].isdigit():
            val = int(line[c]) * 10
            found = True
            break
        else :
            for num in nums:
                if line[c:c+len(num)] == num:
                    val = (nums.index(num) + 1) * 10
                    found = True
                    break
        if found:
            break

    if found:
        found = False
        for c in range(len(line)-1, -1, -1):
            if line[c].isdigit():
                val += int(line[c])
                found = True
                break
            else :
                for num in nums:
                    if line[c-len(num) + 1:c + 1] == num:
                        val += (nums.index(num) + 1)
                        found = True
                        break
            if found:
                break
    
    total += val

print(total)
file.close()