# Task 1: Box calculator

# This table shows each box and the number of items each can hold
# +--------+-------+
# |  Size  | Items |
# +--------+-------+
# | Big    |     5 |
# | Medium |     3 |
# | Small  |     1 |
# +--------+-------+

# Get number of items; assume that the user enters any integer greater than 5
num_items = int(input("How many items do you have? "))

# Calculate minimum number of full boxes needed to store all items

# Initialise box counts to zero
big_box_count = 0
medium_box_count = 0
small_box_count = 0

# Initialise messages to None
big_box_msg = None
medium_box_msg = None
small_box_msg = None

# Calculate number of full big boxes needed, using floor division
# Could also use `divmod()`: https://www.codingem.com/python-floor-division/
big_box_count = int(num_items // 5)

# Work out how many items remain to be boxed up
num_items_remaining = num_items - (big_box_count * 5)

# If there are any over, work out number of full medium boxes needed
if num_items_remaining:
    medium_box_count = int(num_items_remaining // 3)

    num_items_remaining = num_items_remaining - (big_box_count * 3)

    # If there are any over, work out number of full small boxes needed
    if num_items_remaining:
        small_box_count = int(num_items_remaining // 1)

if big_box_count > 1:
    big_box_msg = (str(big_box_count) + " big boxes")
elif big_box_count == 1:
    big_box_msg = "1 big box"
else:
    big_box_msg = None

if medium_box_count > 1:
    medium_box_msg = (str(medium_box_count) + " medium boxes")
elif medium_box_count == 1:
    medium_box_msg = "1 medium box"
else:
    medium_box_msg = None

if small_box_count > 1:
    small_box_msg = (str(small_box_count) + " small boxes")
elif small_box_count == 1:
    small_box_msg = "1 small box"
else:
    small_box_msg = None

# Displays the numbers of big, medium and small boxes used.
print("Those items filled:")
if big_box_msg:
    print(big_box_msg)
if medium_box_msg:
    print(medium_box_msg)
if small_box_msg:
    print(small_box_msg)

# Displays the total number of boxes used.
box_count = int(big_box_count + medium_box_count + small_box_count)
if box_count > 1:
    word = " boxes"
else:
    word = " box"

print("You used " + str(box_count) + word + " in total.")
