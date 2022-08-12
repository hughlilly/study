
# A user should be asked to enter which sport user plays.
# How long the user has been playing that sport (year).
# How many games in total the user has played?
# How many games won. How many games lost.
# How many games were with decision and how many of them were undecided.

sport = input("Which sport do you play? ")
since = int(input("What year did you start playing it? "))
games_played = int(input("How many games have you played? "))
won = int(input("How many did you win? "))
lost = int(input("How many did you lose? "))

playing_years = (2022 - since)
winning_average = ((won/games_played) * 100)
undecided = (games_played - (won + lost))
decided = (games_played - undecided)

print("You've been playing " + str(sport) + " for " + str(playing_years) +
      " years winning an average of " + str(winning_average) + " of them.")

print("You have played " + str(decided) + " games with results announced and " +
      str(undecided) + " games that were undecided.")
