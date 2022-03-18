'''
Task 1: Box calculator

This table shows available box sizes and the number of items each can hold:

+--------+-------+
| Size   | Items |
+--------+-------+
| Big    |     5 |
| Medium |     3 |
| Small  |     1 |
+--------+-------+
'''

# Welcome message and explanation
# Incorporates newline character; uses `\` to keep lines under 80 chars long
print("\nWelcome to the Box Calculator.\nBig boxes hold 5 items; medium boxes hold 3\
 items, and small boxes hold just one item each.\n")

# Get number of items; assume user enters int > 5
num_items = int(input("How many items do you have? "))

# Initialise box counts to zero
big_box_count = 0
medium_box_count = 0
small_box_count = 0

# Initialise messages to None
big_box_msg = ""
medium_box_msg = ""
small_box_msg = ""

# Calculate number of big boxes needed, using floor division (`\\``)
big_box_count = num_items // 5

# Work out how many unboxed items remain; result will be of `int` type
num_items_remaining = num_items - (big_box_count * 5)

# If unboxed items remain, work out number of medium boxes needed
if num_items_remaining:
    medium_box_count = num_items_remaining // 3

    num_items_remaining = num_items_remaining - (medium_box_count * 3)

    '''
    If unboxed items still remain, work out number of small boxes needed
    No need for floor division here:
      (num_items_remaining // 1)
    will always equal `num_items_remaining` itself.
    '''
    if num_items_remaining:
        small_box_count = num_items_remaining


# For each size of box -- if any are used -- print a summary message
# Use plural ("boxes") if more than one, otherwise singular ("box")

print("\nThose items filled:")

if big_box_count > 1:
    print("📦 " + str(big_box_count) + " big boxes")
elif big_box_count == 1:
    print("📦 1 big box")

if medium_box_count > 1:
    print("📦 " + str(medium_box_count) + " medium boxes")
elif medium_box_count == 1:
    print("📦 1 medium box")

if small_box_count > 1:
    print("📦 " + str(small_box_count) + " small boxes")
elif small_box_count == 1:
    print("📦 1 small box")

# Calculate total number of boxes used
box_count = big_box_count + medium_box_count + small_box_count

# If more than one, set string to "boxes", plural, otherwise "box", singular
if box_count > 1:
    box_term = " boxes"
else:
    box_term = " box"

print("\nYou used " + str(box_count) + box_term + " in total.\n")

# This program fulfils the following four test-case assertions:
#
# Test-case A
# -----------
# 22 items should fill:
# 📦 4 big boxes (4 * 5 = 20)
# 📦 2 small boxes (2 * 1 = 2)
# 20 + 2 = 22
# 4 + 2 = 6 boxes total
# -----------
#
# Test-case B
# -----------
# 13 items should fill:
# 📦 2 big boxes (2 * 5 = 10)
# 📦 1 medium box (3 * 1 = 3)
# 10 + 3 = 13
# 2 + 1 = 3 boxes total
# -----------
#
# Test-case C
# -----------
# 9 items should fill:
# 📦 1 big box (5 * 1 = 5)
# 📦 1 medium box (3 * 1 = 3)
# 📦 1 small box (1 * 1 = 1)
# 5 + 3 + 1 = 9
# 1 + 1 + 1 = 3 boxes total
# -----------
#
# Test-case D
# -----------
# 84 items should fill:
# 📦 16 big box (5 * 16 = 80)
# 📦 1 medium box (3 * 1 = 3)
# 📦 1 small box (1 * 1 = 1)
# 80 + 3 + 1 = 84
# 16 + 1 + 1 = 18 boxes total
# -----------
