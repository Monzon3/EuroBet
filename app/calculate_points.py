game_id = 1
goals1 = 2
goals2 = 3
team1_id = 3
team2_id = 5

user_id = 1
bet_goals1 = 2
bet_goals2 = 2
user_team_ids = [1, 5, 9, 11, 18, 22]

# Stablish result of the game
if goals1>goals2:
    result = "1"
elif goals1==goals2:
    result = "x"
else:
    result = "2"

# Stablish result of the game in the bet
if bet_goals1>bet_goals2:
    bet_result = "1"
elif bet_goals1==bet_goals2:
    bet_result = "x"
else:
    bet_result = "2"

# Calculate points for user according to the result of the game
user_result_points = 0
result_flag = 0
if bet_result==result:
    result_flag = 1
    user_result_points = 2    

if result_flag and bet_goals1==goals1:
    user_result_points = user_result_points + 2

if result_flag and bet_goals2==goals2:
    user_result_points = user_result_points + 2

# Calculate points for user according to the teams selected
user_teams_points = 0
if team1_id in user_team_ids:
    if result=="1":
        user_teams_points = user_teams_points + 3
    elif result=="x":
        user_teams_points = user_teams_points + 1

    user_teams_points = user_teams_points + 0.5*goals1

if team2_id in user_team_ids:
    if result=="2":
        user_teams_points = user_teams_points + 3
    elif result=="x":
        user_teams_points = user_teams_points + 1

    user_teams_points = user_teams_points + 0.5*goals2