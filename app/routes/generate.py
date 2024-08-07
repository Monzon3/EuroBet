from fastapi import APIRouter, status
from functions.auxFunctions import *

gen = APIRouter(prefix="/generateDB",
                tags=["""Route to populate the database with all data related to teams, 
                matches and bets."""],
                responses={404: {"description": "Not found"}})

@gen.post("/teams", status_code=status.HTTP_200_OK)
async def import_teams(ranking:dict):
    return import_teams_to_db(ranking)

@gen.post("/games", status_code=status.HTTP_200_OK)
async def import_games(games:list[dict]):
    return import_games_to_db(games)

@gen.post("/bets_games", status_code=status.HTTP_200_OK)
async def import_bets_games(username: str, bets:list[dict]):
    return import_bets_games_to_db(username, bets)

@gen.post("/bets_teams", status_code=status.HTTP_200_OK)
async def import_bets_teams(username: str, bets:dict):
    return import_bets_teams_to_db(username, bets)    