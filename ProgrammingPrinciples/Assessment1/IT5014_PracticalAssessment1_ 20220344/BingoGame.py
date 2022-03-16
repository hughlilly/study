'''
Task 3: Bingo Game

In the game of Bingo, every player has at least one Bingo card like the one
shown below. When a number is called out the player must check this against
the numbers on the card. If a number exists, then it is crossed out.
When all the numbers have been crossed out then the player shouts out “BINGO!!”

This program asks the user to enter integers and checks them against a list
variable standing in for the Bingo card. If a guess is correct, it is removed
from the list, thereby reducing the number of numbers remaining to be guessed.
'''

# Print welcome message and initialise list
print("Welcome to Bingo.")
bingo = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]

# Initialise guess to None; this will be set from user input
guess = None

# While the list contains values (i.e. while `bingo == True`), request guesses
while bingo:
    guess = int(input("Guess a number between 1 and 80: "))

    # Ensure guess is within valid range
    if guess >= 1 and guess <= 80:

        # If the guess is in the list, remove the guess from the list, and print
        # a success message reporting the number of numbers remaining to be guessed
        if guess in bingo:
            bingo.remove(guess)
            print("Correct! You have " + str(len(bingo)) +
                  " numbers left to guess.")

        # If the guess is not in the list, report as much; after this, the "while"
        # condition is tested again.
        else:
            print("Sorry, that's not in the Bingo list. Try again.")
    else:
        print("Sorry, your guess must be between 1 and 80. Try again.")

print("BINGO!")

# This program fulfils the following test-case assertion:
# Given input of `81`, the invalid-guess message is printed.
# Given input of `7`, that number is removed from the list, and the "Correct!"
# statement is printed, along with the number of remaining numbers.
#
# Given after that input of `67`, the failure message is printed, and the
# "while" condition is tested again. Found to be True (i.e., the `bingo` list
# is not empty), another guess is requested. This continues as follows:
#
# +-------+-----------+
# | Guess |  Result   |
# +-------+-----------+
# |    26 | Correct!  |
# |     1 | Incorrect |
# |    40 | Correct!  |
# |    58 | Correct!  |
# |    73 | Correct!  |
# |    14 | Correct!  |
# |     6 | Incorrect |
# |    22 | Correct!  |
# |    34 | Correct!  |
# |    55 | Correct!  |
# |    68 | Correct!  |
# +-------+-----------+
#
# After the last correct guess, the "BINGO!" message is printed. If the list is
# never emptied (in other words, if not all the numbers were correctly guessed),
# the "BINGO!" message after the while condition would never be reached, and the
