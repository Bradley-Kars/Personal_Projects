primes = []

while True:
    try:
        amount = int(input("How many prime numbers would you like to generate?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How many prime numbers would you like to generate?"')

if amount >= 1:
    primes.append(2)
    num = 3 

    while len(primes) < amount:
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 2 

for prime in primes:
    print(prime)