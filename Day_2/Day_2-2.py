with open("Day_2/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0

for i in range (0, len(lines)):
    line = lines[i]
    lead = line.find(": ")
    line = line[lead + 2:]
    color_key = {"red": 0, "green": 0, "blue": 0}

    games = line.split("; ")
    for game in games:
        colors = game.split(", ")
        for color in colors:
            val = color.split(" ")
            if int(val[0]) > color_key[val[1]]:
                color_key[val[1]] = int(val[0])
    total += (color_key["red"] * color_key["green"] * color_key["blue"])

print(total)
file.close()