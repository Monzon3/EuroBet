from functions.database import engine, meta
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

teams_table = Table("Teams", meta,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(20), unique=True, nullable=False))

games_table = Table("Games", meta, 
                    Column("id", Integer, primary_key=True),
                    Column("date", String(10), nullable=False),
                    Column("team1ID", Integer, ForeignKey("Teams.id"), nullable=False),
                    Column("team2ID", Integer, ForeignKey("Teams.id"), nullable=False),
                    Column("goals1", Integer, default = None),
                    Column("goals2", Integer, default = None),
                    Column("result", String(1), default="-"))

users_table = Table("Users", meta,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(20), nullable=False, unique=True),
                    Column("email", String(50), nullable=False, unique=True),
                    Column("password", String(100), nullable=False, unique=True),
                    Column("results_points", Integer, default=0),
                    Column("team_points", Integer, default=0),
                    Column("teamID1", Integer, ForeignKey("Teams.id")),
                    Column("teamID2", Integer, ForeignKey("Teams.id")),
                    Column("teamID3", Integer, ForeignKey("Teams.id")),
                    Column("teamID4", Integer, ForeignKey("Teams.id")),
                    Column("teamID5", Integer, ForeignKey("Teams.id")),
                    Column("teamID6", Integer, ForeignKey("Teams.id")),
                    Column("teamID7", Integer, ForeignKey("Teams.id")),
                    Column("teamID8", Integer, ForeignKey("Teams.id")))

bets_table = Table("Bets", meta,
                   Column("id", Integer, primary_key=True),
                   Column("userID", Integer, ForeignKey("Users.id")),
                   Column("gameID", Integer, ForeignKey("Games.id")),
                   Column("goals1", Integer, nullable=False),
                   Column("goals2", Integer, nullable=False),
                   Column("results_points", Integer, default=0),
                   Column("team_points", Integer, default=0))

meta.create_all(engine)