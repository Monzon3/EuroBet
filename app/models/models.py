from pydantic import BaseModel, Field

class gameData(BaseModel):
    id: int
    date: str = Field(min_length=8, max_length=10)
    team1: str = Field(min_length=1, max_length=20)
    team2: str = Field(min_length=1, max_length=20)

class gameResult(BaseModel):
    id: int
    goals1: int
    goals2: int

class betGame(gameResult):
    ''' Just a copy of gameResult class '''

class groupTable(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    played: int
    won: int
    drawn: int 
    lost: int
    goals_for: int
    goals_against: int
    points: int

class team(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=20)
    group: str = Field(min_length=1, max_legnth=1)