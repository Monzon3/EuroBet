from configparser import ConfigParser
from functions.dbConnector import engine
import json
from models import bets_table, games_table, teams_table, users_table
from sqlalchemy import insert, select

def import_games_to_db(games:dict):
    for i in games.keys():
        team1ID = select(teams_table.c.id).where(teams_table.c.name == games[i]['team1'])
        team2ID = select(teams_table.c.id).where(teams_table.c.name == games[i]['team2'])
        query = insert(games_table).values(date=games[i]['date'], 
                                           team1ID=team1ID, team2ID=team2ID,
                                           result="-")
        with engine.begin() as conn:
            conn.execute(query)


def import_teams_to_db(ranking:dict):
    for i in ranking.keys():
        query = insert(teams_table).values(id=ranking[i], name=i)
        with engine.begin() as conn:
            conn.execute(query)


def import_bets_to_db(username:str, bets: dict):    
    for i in bets.keys():
        userID = select(users_table.c.id).where(users_table.c.name==username)
        query = insert(bets_table).values(userID=userID,
                                          gameID=i,
                                          goals1=bets[i]['goals1'], goals2=bets[i]['goals2'])
        with engine.begin() as conn:
            conn.execute(query)   