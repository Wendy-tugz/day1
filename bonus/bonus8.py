# date = input("Enter today's date: ")
# mood = input("How do you rate your mood from 1 to 10: ")
# thoughts = input("Let your thoughts flow:\n ")
#
#
# with open(f"../journal/{date}.txt", "w") as file:
#     file.write(mood + '\n')
#     file.write(thoughts)





while True:
    with open("../files/sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ") + "\n"

    sides.append(side)

    with open("../files/sides.txt", 'w') as file:
        file.writelines(sides)

    p_heads = sides.count("head\n")
    percentage = p_heads / len(sides) * 100

    print(f"Heads: {percentage}%")

