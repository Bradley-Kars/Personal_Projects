print("Loan Calculator")
print()
while True:
    try:
        loan = float(input("How much did you borrow?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How much did you borrow?"')
while True:
    try:
        interest = float(input("What is your annual interest rate?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "What is your annual interest rate?"')
while True:
    try:
        years = int(input("How many years is the loan for?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How many years is the loan for?"')
annual_interest_rate = interest / 100
total_payments = years
fixed_payment = loan * (annual_interest_rate * (1 + annual_interest_rate) ** total_payments) / ((1 + annual_interest_rate) ** total_payments - 1)
monthly_payment = fixed_payment / 12
formatted_interest = '{:.2f}%'.format(interest)
counter = 0
print()
print(f"You have taken out a {years}-year loan of ${loan:.2f} at an interest rate of {formatted_interest} APR.")
print()
print(f"To pay off the loan completely in {years} years, you need to make annual payments of ${fixed_payment:.2f} or a monthly payments of ${monthly_payment:.2f}.")
print()
print("Assuming you make these fixed annual payments, you'll owe:")
for year in range(1, years + 1):
    interest_payment = loan * annual_interest_rate
    principal_payment = fixed_payment - interest_payment
    loan -= principal_payment
    counter += 1
    print(f"End of year {counter}, you owe ${loan:.2f}")
print()
print("Congratulations! The loan is paid off.")