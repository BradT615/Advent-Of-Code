with open("Day_4/input.txt", "r") as file:
    total = 0

    for line in file:
        line = line.strip().split(": ")[1]  # Directly split and take the second part
        winningCards, yourCards = [set(cards.split()) for cards in line.split("|")]
        matches = len(winningCards.intersection(yourCards))

        if matches > 0:
            total += 2 ** (matches - 1)

    print(total)
