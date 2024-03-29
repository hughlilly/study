# A2: Parking meter

# Test case, if the user parks for 5 hours:
# First 3 hours = 3h * $4 = $12
# Next 2 hours  = 2h * $3 = $6
# Total = $18

print("Kia ora, welcome to the parking meter")

normal_rate = 4
discounted_rate = normal_rate * .75
total = 0

num_hours = int(input("How many hours did you park today? "))

if num_hours > 3:
    base_fee = normal_rate * 3
    discounted_hours = num_hours - 3
    discounted_fee = discounted_hours * discounted_rate
    total = base_fee + discounted_fee
else:
    total = num_hours * normal_rate

print("Your fee is $" + str(int(total)))
