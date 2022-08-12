# A4: Password reset app

# Set correct email, initialise `reset` and `failed` to False, and `attempts` to zero
valid_email = "user@domain.com"
reset = False
failed = False
attempts = 0

# While it is not true that the password has been reset or that resetting has
# failed because of too many attempts, ask for inputs

while not reset and not failed:
    user_email = input("Please enter your email address: ")
    confirmed_email = input("Enter it again to confirm: ")

    # Compare inputs to stored variable
    is_match = user_email == valid_email and confirmed_email == valid_email

    # If inputs match, print "Correct" and set `reset` to True, exiting the loop
    if is_match:
        print("Correct.")
        reset = True

    # Else, if they don't match, increment `attempts`
    elif attempts < 2:
        print("Sorry, those didn't match; please try again.")
        attempts += 1
    # Else, there have been more than two attempts
    else:
        print("Sorry, too many attempts. Try again later.")
        failed = True
