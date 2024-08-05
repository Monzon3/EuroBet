from fastapi import APIRouter, status
from functions.auxFunctions import *

gen = APIRouter(prefix="/generateDB",
                tags=["""Route to populate the database, inserting all data related to teams, 
                matches and bets."""],
                responses={404: {"description": "Not found"}})

@gen.post("/ranking", status_code=status.HTTP_200_OK)
async def upload_rankingFifa(ranking:dict):
    return import_teams_to_db(ranking)

@gen.post("/games", status_code=status.HTTP_200_OK)
async def upload_allGames(games:dict):
    return import_games_to_db(games)

@gen.post("/bets", status_code=status.HTTP_200_OK)
async def upload_bets(username: str, bets:dict):
    return import_bets_to_db(username, bets)