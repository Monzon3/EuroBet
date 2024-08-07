from functions.dbConnector import engine
from models.models import gameResult
import pandas as pd
from tables import games_table, teams_table
from sqlalchemy import select, update

def get_group_table_from_db(group: str):
    query = select(teams_table.c['name', 'played', 
                                 'won', 'drawn', 'lost', 
                                 'goals_for', 'goals_against'])\
            .where(teams_table.c.group==group)

    with engine.begin():
        teams = pd.read_sql(query, con=engine)

    teams['goal_difference'] = teams['goals_for'] - teams['goals_against']
    teams['points'] = teams['won']*3 + teams['drawn']*1
    
    order_by = ['points', 'goals_for', 'goal_difference']
    teams = teams.sort_values(by=order_by, ascending=[False, False, True])

    return teams.to_dict('records')

def import_results_to_db(games:list[gameResult]):
    for game in games:
        gameID = game.id
        goals1 = game.goals1
        goals2 = game.goals2

        # First, get result of the match and update the Games table
        query = update(games_table)\
                .values(goals1=goals1, goals2=goals2)\
                .where(games_table.c.id==gameID)
                
        with engine.begin() as conn:
            conn.execute(query)

        if goals1>goals2:
            match_result = "1"
        elif goals1<goals2:
            match_result = "2"
        else:
            match_result = "x"

        # Obtain the teams that have played
        query = select(games_table.c['team1ID', 'team2ID']).where(games_table.c.id==gameID)
        with engine.connect() as conn:
            res = conn.execute(query).fetchone()

        team1ID = res.team1ID
        team2ID = res.team2ID

        # Update teams with goals and results
        if match_result=="1":
            query1 = update(teams_table)\
                     .where(teams_table.c.id==team1ID)\
                     .values(played=teams_table.c.played+1, won=teams_table.c.won+1, 
                             goals_for=teams_table.c.goals_for+goals1, 
                             goals_against=teams_table.c.goals_against+goals2)

            query2 = update(teams_table)\
                     .where(teams_table.c.id==team2ID)\
                     .values(played=teams_table.c.played+1, lost=teams_table.c.lost+1, 
                             goals_for=teams_table.c.goals_for+goals2, 
                             goals_against=teams_table.c.goals_against+goals1)                
        elif match_result=="2":
            query1 = update(teams_table)\
                     .where(teams_table.c.id==team1ID)\
                     .values(played=teams_table.c.played+1, lost=teams_table.c.lost+1, 
                             goals_for=teams_table.c.goals_for+goals1, 
                             goals_against=teams_table.c.goals_against+goals2)

            query2 = update(teams_table)\
                     .where(teams_table.c.id==team2ID)\
                     .values(played=teams_table.c.played+1, won=teams_table.c.won+1, 
                             goals_for=teams_table.c.goals_for+goals2, 
                             goals_against=teams_table.c.goals_against+goals1) 
        else:
            query1 = update(teams_table)\
                     .where(teams_table.c.id==team1ID)\
                     .values(played=teams_table.c.played+1, drawn=teams_table.c.drawn+1, 
                             goals_for=teams_table.c.goals_for+goals1, 
                             goals_against=teams_table.c.goals_against+goals2)

            query2 = update(teams_table)\
                     .where(teams_table.c.id==team2ID)\
                     .values(played=teams_table.c.played+1, drawn=teams_table.c.drawn+1, 
                             goals_for=teams_table.c.goals_for+goals2, 
                             goals_against=teams_table.c.goals_against+goals1)  

        with engine.begin() as conn:
            # Try to do this two queries in just one execute
            conn.execute(query1)
            conn.execute(query2)