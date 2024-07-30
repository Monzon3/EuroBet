from functions.dbConnector import conn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
#from routes.games import gms
#from routes.other import oth
#from routes.users import usr

description = """
## This is an API to manage the EuroCup 2024 bet."""

app = FastAPI(
    title="EuroCup 2024 API",
    description=description,
    contact={"name": "Sergio Monzón", "email": "sergio.monzon3@gmail.com"}
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
#app.include_router(gms)
#app.include_router(oth)
#app.include_router(flm)

@app.get("/")
async def root():
    return {"Info": "Go to /docs URL for more info on the API"}