sport = "Badminton" #this is an string variable
starting_year = 2010 #this is an integer variable
total_games = 80
won = 50
lost = 20
playing_time = 2022 - starting_year #this will give me information about total_years
winning_average = (won/total_games) * 100
without_result = total_games - won - lost
with_result = won + lost
print("You have been playing " + sport + "for " + str(playing_time) + "years with winning average " + str(winning_average))

