from configparser import ConfigParser
from database import engine
import json
from models import games_table, teams_table
from sqlalchemy import insert

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