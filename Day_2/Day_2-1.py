with open("Day_2/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
color_key = {"red": 12, "green": 13, "blue": 14}

for i in range (0, len(lines)):
    line = lines[i]
    lead = line.find(": ")
    line = line[lead + 2:]
    print(line, "\n")
    Valid = True

    games = line.split("; ")
    for game in games:
        colors = game.split(", ")
        for color in colors:
            val = color.split(" ")   
            if val[1] in color_key and int(val[0]) > color_key[val[1]]:
                Valid = False
                break
    if Valid:
        total += i + 1

print(total)
file.close()