import collections
import random

def invert_percentage(percentage):
    return 100 - percentage

def all_same_percentage(percentage_dict):
    return len(set(percentage_dict.values())) == 1

num_random_numbers = int(input("Enter the number of random numbers to generate: "))

random_numbers = [random.randint(0, 9) for _ in range(num_random_numbers)]

iteration = 0

while True:
    number_counts = collections.Counter(random_numbers)
    total_numbers = len(random_numbers)
    percentage_dict = {number: (count / total_numbers) * 100 for number, count in number_counts.items()}

    if all_same_percentage(percentage_dict):
        print(f"Final result after {iteration} iterations:")
        for number, percentage in sorted(percentage_dict.items()):
            print(f"{number}: {percentage:.2f}%")
        organized_result = ', '.join(map(str, sorted(random_numbers)))
        print(f"Numbers: {organized_result}")
        break

    inverted_percentage_dict = {number: invert_percentage(percentage) for number, percentage in percentage_dict.items()}
    total_inverted_percentage = sum(inverted_percentage_dict.values())
    new_percentage_dict = {number: (inverted_percentage / total_inverted_percentage) * 100 for number, inverted_percentage in inverted_percentage_dict.items()}

    new_random_numbers = []
    for number, new_percentage in new_percentage_dict.items():
        count = int((new_percentage / 100) * total_numbers)
        new_random_numbers.extend([number] * count)

    while len(new_random_numbers) < num_random_numbers:
        new_random_numbers.append(random.choice(list(new_percentage_dict.keys())))

    random.shuffle(new_random_numbers)

    organized_result = ', '.join(map(str, sorted(new_random_numbers)))
    print(f"Iteration {iteration}: Generated new random numbers based on adjusted percentages:")
    print(organized_result)

    print("New percentages after inversion:")
    for number, percentage in sorted(new_percentage_dict.items()):
        print(f"{number}: {percentage:.2f}%")

    random_numbers = new_random_numbers
    iteration += 1
