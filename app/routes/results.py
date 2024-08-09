from fastapi import APIRouter, status
from functions.resultsFunctions import *
from models.models import gameResult

res = APIRouter(prefix="/insert-results",
                tags=["""Route to insert results of the games as they are played,
                and populate secondary tables."""],
                responses={404: {"description": "Not found"}})

@res.post("/games", status_code=status.HTTP_200_OK)
async def import_games_results(games:list[gameResult]):
    return import_results_to_db(games)   

@res.post("/group_table", status_code=status.HTTP_200_OK)
async def get_group_table(group: str):
    return get_group_table_from_db(group=group)