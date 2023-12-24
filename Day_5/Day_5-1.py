with open("Day_5/input.txt", "r") as file:
    lines = [line.strip() for line in file]
    seeds = lines[0].strip().split()[1:]

    for i, line in enumerate(lines):
        print(lines[i])
    print(seeds)
