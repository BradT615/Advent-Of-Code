with open("Day_4/input.txt", "r") as file:
    lines = [line.strip() for line in file]

    total = 0
    for i in range(0, len(lines)):
        matches = 0
        line = lines[i]
        lead = line.find(": ")
        line = line[lead + 2:]
        cards = line.split("|")
        winningCards = cards[0].split()
        yourCards = cards[1].split()
        for card in winningCards:
            for yourCard in yourCards:
                if card == yourCard:
                    matches += 1
        if matches > 0:
            total += 2 ** (matches - 1)
        
    print(total)
    file.close()