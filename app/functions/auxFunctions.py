from configparser import ConfigParser
#from database import engine
import json
from models import bets_table, games_table, teams_table, users_table
from sqlalchemy import insert, select

def import_games_to_db():
    # Load the configuration.ini file
    config = ConfigParser()
    config.read('../config/configuration.ini')

    list_games = config.get('main_files', 'games_list')
    with open(list_games, encoding = 'utf-8') as f:
        games = json.load(f)

    teams_ranking = config.get('main_files', 'fifa_ranking')
    with open(teams_ranking, encoding = 'utf-8') as f:
        ranking = json.load(f)

    for i in games.keys():
        query = insert(games_table).values(date=games[i]['date'], 
                                           team1ID=ranking[games[i]['team1']], team2ID=ranking[games[i]['team2']],
                                           result="-")
        with engine.begin() as conn:
            conn.execute(query)


def import_teams_to_db():
    # Load the configuration.ini file
    config = ConfigParser()
    config.read('../config/configuration.ini')

    teams_ranking = config.get('main_files', 'fifa_ranking')
    with open(teams_ranking, encoding = 'utf-8') as f:
        ranking = json.load(f)

    for i in ranking.keys():
        query = insert(teams_table).values(name=i)
        with engine.begin() as conn:
            conn.execute(query)

def import_bets_to_db(username:str):
    # Load all bets for a specific user
    config = ConfigParser()
    config.read('../config/configuration.ini')

    # Get user's ID
    with engine.begin() as conn:
        res = conn.execute(select(users_table.c.id).where(users_table.c.name==username)).first()
        user_ID = res[0]
    
    bets_file = config.get('bet_files', f'bets_{username}')
    with open(bets_file, encoding = 'utf-8') as f:
        bets = json.load(f)

    for i in bets.keys():
        query = insert(bets_table).values(userID=user_ID,
                                          gameID=i,
                                          goals1=bets[i]['goals1'], goals2=bets[i]['goals2'])
        with engine.begin() as conn:
            conn.execute(query)   