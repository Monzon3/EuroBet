from functions.dbConnector import engine
from models import bets_table, games_table, teams_table, users_table
from sqlalchemy import insert, select, update, bindparam

def import_games_to_db(games:list[dict]):
    for game in games:
        scalar1 = (select(teams_table.c.id)\
                   .where(teams_table.c.name==bindparam("team1")).scalar_subquery())
        scalar2 = (select(teams_table.c.id)\
                   .where(teams_table.c.name==bindparam("team2")).scalar_subquery())

        values_to_db = {"id": game['id'],
                        "team1": game['team1'],
                        "team2": game['team2'],
                        "date": game['date'],
                        "goals1": 0, "goals2": 0}  

        with engine.begin() as conn:
            conn.execute(insert(games_table)\
                         .values(team1ID=scalar1, team2ID=scalar2), values_to_db)


def import_teams_to_db(ranking:dict):
    for i in ranking.keys():
        values_to_db = {"id": i, 
                        "name": ranking[i]['name'],
                        "group": ranking[i]['group'],
                        "played": 0, 
                        "won": 0, 
                        "drawn": 0, 
                        "lost": 0,
                        "goals_for": 0, 
                        "goals_against": 0}

        with engine.begin() as conn:
            conn.execute(insert(teams_table), values_to_db)


def import_bets_games_to_db(username:str, bets:list[dict]):    
    for bet in bets:
        userID = select(users_table.c.id)\
                 .where(users_table.c.name==bindparam("username")).scalar_subquery()

        values_to_db = {"username": username,
                        "gameID": bet['id'],
                        "goals1": bet['goals1'],
                        "goals2": bet['goals2']}

        with engine.begin() as conn:
            conn.execute(insert(bets_table).values(userID=userID), values_to_db)

def import_bets_teams_to_db(username: str, bets: dict):
    userID = select(users_table.c.id).where(users_table.c.name==username)
    team1ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][0])
    team2ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][1])
    team3ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][2])
    team4ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][3])
    team5ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][4])
    team6ID = select(teams_table.c.id).where(teams_table.c.name==bets['teams'][5])
    more_goals1 = select(teams_table.c.id).where(teams_table.c.name==bets['more_goals_for'])
    less_goals1 = select(teams_table.c.id).where(teams_table.c.name==bets['less_goals_for'])
    more_goals2 = select(teams_table.c.id).where(teams_table.c.name==bets['more_goals_against'])
    less_goals2 = select(teams_table.c.id).where(teams_table.c.name==bets['less_goals_against'])
    winner = select(teams_table.c.id).where(teams_table.c.name==bets['winner'])
    more_goals3 = select(teams_table.c.id).where(teams_table.c.name==bets['more_goals_total'])
    
    values_to_db = {
              "team1ID": team1ID,
              "team2ID": team2ID,
              "team3ID": team3ID,
              "team4ID": team4ID,
              "team5ID": team5ID,
              "team6ID": team6ID,
              "more_goals_for": more_goals1,
              "less_goals_for": less_goals1,
              "more_goals_against": more_goals2,
              "less_goals_against": less_goals2,
              "winner": winner,
              "more_goals_total": more_goals3}
    
    query = update(users_table).where(users_table.c.id==1).values(values_to_db)
                    
    with engine.begin() as conn:
        conn.execute(query) 