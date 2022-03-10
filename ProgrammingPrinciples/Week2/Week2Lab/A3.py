# A3: Bonus count system

# Test case:
# Basic salary = $5000
# Sales amount = $3500
# Total amount = $5250 ($5000 + $250 bonus)

# Ask employee their salary and sales amount
salary = int(input("What is your salary? $"))
sales = int(input("What did you make in sales this year? $"))

# Calculate bonus
if sales <= 2500:
    bonus = 150
elif sales > 2500:
    bonus = 250
elif sales > 5000:
    bonus = 350
elif sales > 10000:
    bonus = 500

total = salary + bonus

print("Your total compensation is $" + str(total))
