import os

input_number = int(input("Enter your starting amount between 0 and 50000: "))
while input_number > 50000 or input_number < 0:
    print("Enter a value in the acceptable range please. ")
    input_number == int(input("Please try again. "))
interest_rate = int(input("Enter your Interest Rate between 0 and 15: "))
while interest_rate > 15 or interest_rate < 0:
    print("Enter a value in the acceptable range please. ")
    interest_rate == int(input("Please enter a value in the range please. "))
investment_time = int(input("Enter the duration of your investment. "))
while investment_time <= 0:
    print("enter the investment duration")

total = input_number
months = investment_time * 12
monthly_rate = interest_rate / 12 / 100

#  I think this is right, im not fully sure..

for month in range(1, months + 1):
    total += input_number
    interest = round(total * monthly_rate, 2)
    total += interest
    if month % 12 == 0:
        print(f"year {month // 12}: ${total:} ")

# I think this is right again, it outputs, just with too many decimal points..

print(f"investment duration: {investment_time} years")
print(f"Yearly interest rate: {interest_rate}%")
print(f"Monthly investment amount: ${input_number:}")
print(f"Total investment amount: ${total:}")

os.system("pause")