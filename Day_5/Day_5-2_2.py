def process_map(map_list):
    map_dict = {}
    for line in map_list:
        dest_start, src_start, range_length = map(int, line.split())
        for offset in range(range_length):
            map_dict[src_start + offset] = dest_start + offset
    return map_dict

with open("Day_5/input.txt", "r") as file:
    lines = [line.strip() for line in file]
    seeds = lines[0].strip().split()[1:]

    # Process the maps first
    i = 1  # Start from line 1 as line 0 is seeds
    map_dicts = []
    while i < len(lines):
        if 'map:' in lines[i]:
            i += 1  # Skip the line containing 'map:'
            map_list = []
            while i < len(lines) and lines[i] != "":
                map_list.append(lines[i])
                i += 1
            map_dicts.append(process_map(map_list))
        else:
            i += 1

    # Generate new seeds and map them
    min_location = float('inf')
    for i in range(0, len(seeds), 2):
        for count in range(int(seeds[i + 1])):
            seed = int(seeds[i]) + count
            for map_dict in map_dicts:
                seed = map_dict.get(seed, seed)  # Get mapped value or keep the same
            min_location = min(min_location, seed)

    print(min_location)
