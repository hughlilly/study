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


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NegativeNumber(Error):
    __module__ = 'builtins'
    """Raised when the input value is non-positive"""
    pass


def calculate_small_boxes(number: int) -> int:
    """Calculates the number of small boxes (these hold just one item each).

    Parameters:
    `number` : int, required
        The number of items to put into small boxes
    Returns:
        int
    """
    # Small box count will be whatever is left over after dividing
    # the (remaining) number of items by 3
    if number > 0:
        return number if number < 3 else None
    elif number < 0:
        raise NegativeNumber("Needed a positive number.")


def calculate_medium_boxes(number: int) -> int:
    """Calculates the number of medium boxes (these hold 3 items each).

    Parameters:
    `number` : int, required
        The number of items to put into medium boxes
    Returns:
        int
    """
    if number > 0:
        return number // 3
    elif number < 0:
        raise NegativeNumber("Needed a positive number.")
    return number


def calculate_big_boxes(number: int) -> int:
    """Calculates the number of big boxes (these hold 5 items each).

    Parameters:
    `number` : int, required
        The number of items to put into big boxes
    Returns:
        int
    """
    if number > 0:
        return number // 5
    elif number < 0:
        raise NegativeNumber("Needed a positive number.")
    return number


def calculate_boxes(num_items: int):
    """Calculates the number of boxes of various sizes filled by a given\
        number of items.

    Parameters:
    `num_items` : int, required
        The number of items to put into boxes
    """
    # Initialise box counts to zero
    big_box_count = 0
    medium_box_count = 0
    small_box_count = 0
    num_items_remaining = 0

    # Count number of big boxes filled
    big_box_count = calculate_big_boxes(num_items)

    # Work out how many unboxed items remain
    num_items_remaining = num_items % 5

    # Count number of medium boxes filled
    medium_box_count = calculate_medium_boxes(num_items_remaining)

    # Count number of small boxes filled
    small_box_count = calculate_small_boxes(num_items_remaining % 3)

    # For each size of box, print a summary message
    # Use plural ("boxes") if more than one, otherwise singular ("box")

    print("\nThat number of items filled:")

    if big_box_count:
        if big_box_count > 1:
            print("📦 " + str(big_box_count) + " big boxes")
        elif big_box_count == 1:
            print("📦 1 big box")

    if medium_box_count:
        if medium_box_count > 1:
            print("📦 " + str(medium_box_count) + " medium boxes")
        elif medium_box_count == 1:
            print("📦 1 medium box")

    # Add up the number of items to put into boxes used
    box_count = big_box_count + medium_box_count

    # If any small boxes were used, print a message about them and add
    # their number to the overall count
    if small_box_count:
        if small_box_count > 1:
            print("📦 " + str(small_box_count) + " small boxes")
        elif small_box_count == 1:
            print("📦 1 small box")
        box_count += small_box_count

    # If more than one, set string to "boxes", plural, otherwise "box",
    # singular, using ternary operator
    box_term = " boxes" if box_count > 1 else " box"

    print("\nYou used " + str(box_count) + box_term + " in total.\n")
    # End of program


# The name/main guard ensures this code will be run only when this file
# is directly executed/called

def get_integer():
    user_input = 0
    user_input = input("How many items do you have? ")
    try:
        int(user_input)
    except ValueError:
        raise ValueError("Sorry, we needed an integer.")
    return int(user_input)


if __name__ == "__main__":

    # Welcome message and explanation
    print("Welcome to the Box Calculator.\nBig boxes hold 5 items; medium boxes hold 3 items, and small boxes hold just one item each.")
    print("Please enter a positive integer.")

    while True:
        # Get number of items
        num_items = get_integer()
        calculate_boxes(num_items)
