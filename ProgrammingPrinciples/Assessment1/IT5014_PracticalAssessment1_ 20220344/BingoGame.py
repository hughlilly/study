'''
Task 3: Bingo Game

In the game of Bingo, every player has at least one Bingo card which contains a
series of numbers. When a number is called out, the player must check it
against the numbers on their card. If the number is there, it gets crossed out.
When all their numbers have been crossed out, the player shouts out “BINGO!”

This program reverses the process somewhat: it asks the user to enter integers,
and checks them against a list variable standing in for the Bingo card.
If a guess is correct, it is removed from the list, thereby reducing the number
of Bingo numbers remaining to be guessed.
'''

# Print welcome message and initialise list
print("\nWelcome to Bingo.")
bingo = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]

# While the list contains values (i.e. while `bingo == True`), request guesses
while bingo:
    # Cast input to an integer; no error-handling for any other input types
    guess = int(input("\nGuess a number between 1 and 80: "))

    # Ensure guess is within valid range
    if guess >= 1 and guess <= 80:

        # If the guess is in the list, remove the guess from the list, and
        if guess in bingo:
            bingo.remove(guess)

            # Test if `bingo` still contains values; if the last value has been
            # removed (thereby making the list empty), the program will go
            # straight to the "BINGO!" message after the `while` loop
            if bingo:
                # Print success message with number of numbers remaining
                print("Correct! You have " + str(len(bingo)) +
                      " numbers left to guess.")

        # If the guess is not in the list, report as much; after this, the
        # "while" condition is tested again
        else:
            print("Sorry, that's not in the Bingo list. Try again.")

    # If input is invalid, print error message; after this, the "while"
    # condition is tested again
    else:
        print("Sorry, your guess must be between 1 and 80. Try again.")

print("BINGO!\n")

'''
This program fulfils the following test-case assertion:
Given input of `92`, the invalid-guess message is printed.
Given input of `0`, the invalid-guess message is printed.
Given input of `7`, that number is removed from the list, and the success
message is printed, along with the number of remaining numbers (9).

Given after that input of `67`, the failure message is printed, and the
"while" condition is tested again. Found to be True -- i.e., the `bingo`
list contains values/is not empty -- another guess is requested.

This continues as follows:
+-------+-----------+
| Guess |  Result   |
+-------+-----------+
|    26 | Correct!  |
|     1 | Incorrect |
|    40 | Correct!  |
|    58 | Correct!  |
|    73 | Correct!  |
|    14 | Correct!  |
|     6 | Incorrect |
|    22 | Correct!  |
|    34 | Correct!  |
|    55 | Correct!  |
|    68 | Correct!  |
+-------+-----------+

After the last correct guess, the "BINGO!" message is printed.

If the list is never emptied -- i.e., if the numbers have not all been
correctly guessed -- the "BINGO!" message is not evaluated. The game will not
end until all the numbers have been correctly guessed; the user is therefore
allowed an infinite number of guesses.

NB: In its current state, this program does not account for the user guessing
a correct number twice; for example, `26` followed by `26` will yield the
success message followed by the "Sorry…" message. A better experience would
be to say "That number has already been guessed" on the second attempt.
This could be the case even if the number was incorrect.
'''
