with open("Day_5/input.txt", "r") as file:
    lines = [line.strip() for line in file]
    seeds = lines[0].strip().split()[1:]
    seedlocations = seeds

    mapArray = []
    # for i in range(len(lines)):

    # i = 0

    # while i < len(lines) and 'map:' not in lines[i]:
    #     i += 1
    # i += 1
    # while i < len(lines) and lines[i] != "":
    #     mapArray.append(lines[i])
    #     i += 1

    # print('seeds:')
    # print(seeds)
    # print('map:')
    # print(mapArray[:50])
    # mapArray = []

    # while i < len(lines) and 'map:' not in lines[i]:
    #     i += 1
    # i += 1
    # while i < len(lines) and lines[i] != "":
    #     mapArray.append(lines[i])
    #     i += 1

    # print('seeds:')
    # print(seeds)
    # print('map:')
    # print(mapArray[:50])

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
        for i in range(2):
            print(seeds[i])
            for line in subArray:
                print(line)
        break