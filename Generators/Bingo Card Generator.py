import random

def prettyPrint():
    for i, row in enumerate(bingo_card):
        for j, cell in enumerate(row):
            if i == 0:
                if j == 4:
                    print(str(cell).center(12), end=' ')
                else:
                    print(str(cell).center(12), end=' | ')
            elif cell == "Free Space":
                print(cell.center(12), end=' | ')
            else:
                if j < 4:
                    print(f'{str(cell).center(12)} |', end=' ')
                else:
                    print(f'{str(cell).center(12)}', end=' ')
        if i < 5:
            print("\n" + "-" * 14 * 5)
        else:
            print()

print("Bingo Card Generator")

bingo_card = [["B", "I", "N", "G", "O"],
              [None, None, None, None, None],
              [None, None, None, None, None],
              [None, None, "Free Space", None, None],
              [None, None, None, None, None],
              [None, None, None, None, None]]

generated_numbers = set()

for col in range(5):
    for row in range(5):
        if bingo_card[row + 1][col] is None:  # Skip the first row with "BINGO"
            lower_bound = col * 15 + 1
            upper_bound = lower_bound + 14 if col < 4 else lower_bound + 10  # Adjust upper bound for 'O' column
            while True:
                random_number = random.randint(lower_bound, upper_bound)
                if random_number not in generated_numbers:
                    bingo_card[row + 1][col] = random_number
                    generated_numbers.add(random_number)
                    break

print()
prettyPrint()
