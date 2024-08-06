from fastapi import APIRouter, status
from functions.resultsFunctions import *

res = APIRouter(prefix="/insert-results",
                tags=["""Route to insert results of the games as they are played,
                and populate secondary tables."""],
                responses={404: {"description": "Not found"}})

@res.post("/games", status_code=status.HTTP_200_OK)
async def import_games(games:list[dict]):
    return import_results_to_db(games)   