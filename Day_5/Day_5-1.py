with open("Day_5/input.txt", "r") as file:
    lines = [line.strip() for line in file]
    seeds = lines[0].strip().split()[1:]

    mapArray = []

    i = 0
    while i < len(lines):
        mapArray = []

        while i < len(lines) and 'map:' not in lines[i]:
            i += 1
        i += 1  # Skip the line containing 'map:'

        while i < len(lines) and lines[i] != "":
            mapArray.append(lines[i])
            i += 1

        subArray = [list(map(int, item.split())) for item in mapArray]
        for j in range(len(seeds)):
            seed = int(seeds[j])
            for line in subArray:
                if seed > line[1] and seed < (line[1] + (line[2] - 1)):
                    seeds[j] = seed + (line[0] - line[1])

    print(min(seeds))