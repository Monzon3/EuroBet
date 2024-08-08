from functions.dbConnector import engine, meta
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

teams_table = Table("Teams", meta,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(20), unique=True, nullable=False),
                    Column("group", String(1), nullable=False),
                    Column("played", Integer, nullable=False), 
                    Column("won", Integer, nullable=False),
                    Column("drawn", Integer, nullable=False),
                    Column("lost", Integer, nullable=False),
                    Column("goals_for", Integer, nullable=False),
                    Column("goals_against", Integer, nullable=False),
                    #Column("goal_difference", Integer, nullable=False),
                    #Column("pts_league", Integer, nullable=False),
                    #Column("pts_knockout", Integer, nullable=False)
                    )

games_table = Table("Games", meta, 
                    Column("id", Integer, primary_key=True),
                    Column("date", String(10), nullable=False),
                    Column("team1ID", Integer, ForeignKey("Teams.id"), nullable=False),
                    Column("team2ID", Integer, ForeignKey("Teams.id"), nullable=False),
                    Column("goals1", Integer, default = None),
                    Column("goals2", Integer, default = None),
                    #Column("result", String(1), default="-"))
                    )

users_table = Table("Users", meta,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(20), nullable=False, unique=True),
                    Column("email", String(50), nullable=False, unique=True),
                    Column("password", String(100), nullable=False, unique=True),
                    #Column("results_points", Integer, default=0),
                    #Column("teams_points", Integer, default=0),
                    Column("team1ID", Integer, ForeignKey("Teams.id")),
                    Column("team2ID", Integer, ForeignKey("Teams.id")),
                    Column("team3ID", Integer, ForeignKey("Teams.id")),
                    Column("team4ID", Integer, ForeignKey("Teams.id")),
                    Column("team5ID", Integer, ForeignKey("Teams.id")),
                    Column("team6ID", Integer, ForeignKey("Teams.id")),
                    Column("more_goals_for", Integer, ForeignKey("Teams.id")),
                    Column("less_goals_for", Integer, ForeignKey("Teams.id")),
                    Column("more_goals_against", Integer, ForeignKey("Teams.id")),
                    Column("less_goals_against", Integer, ForeignKey("Teams.id")),
                    Column("winner", Integer, ForeignKey("Teams.id")),
                    Column("more_goals_total", Integer, ForeignKey("Teams.id")))

users_pts_table = Table("UsersPoints", meta, 
                        Column("userID", ForeignKey("Users.id"), primary_key=True, ),
                        Column("results_points", Integer),
                        Column("teams_points", Integer),
                        Column("Day1", Integer),
                        Column("Day2", Integer),
                        Column("Day3", Integer),
                        Column("Day4", Integer),
                        Column("Day5", Integer),
                        Column("Day6", Integer),
                        Column("Day7", Integer),
                        Column("Day8", Integer),
                        Column("Day9", Integer),
                        Column("Day10", Integer),
                        Column("Day11", Integer),
                        Column("Day12", Integer),
                        Column("Day13", Integer),
                        Column("Day14", Integer),
                        Column("Day15", Integer),
                        Column("Day16", Integer),
                        Column("Day17", Integer),
                        Column("Day18", Integer),
                        Column("Day19", Integer),
                        Column("Day20", Integer),
                        Column("Day21", Integer),
                        Column("Day22", Integer))

bets_table = Table("Bets", meta,
                   Column("id", Integer, primary_key=True),
                   Column("userID", Integer, ForeignKey("Users.id"), nullable=False),
                   Column("gameID", Integer, ForeignKey("Games.id"), nullable=False),
                   Column("goals1", Integer, nullable=False),
                   Column("goals2", Integer, nullable=False),
                   #Column("results_points", Integer, default=0),
                   #Column("team_points", Integer, default=0))
                   )

meta.create_all(engine)