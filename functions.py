from configparser import ConfigParser
import json

def import_games_to_db():
    # Load the configuration.ini file
    config = ConfigParser()
    config.read('./config/configuration.ini')

    list_games = config.get('main_files', 'games_list')
    with open(list_games, encoding = 'utf-8') as f:
        games = json.load(f)

    teams_ranking = config.get('main_files', 'fifa_ranking')
    with open(teams_ranking, encoding = 'utf-8') as f:
        ranking = json.load(f)

    for i in games.keys():
        print(f"GameID: {i}")
        print(f"Team1: {games[i]['team1']} - {ranking[games[i]['team1']]}")
        print(f"Team2: {games[i]['team2']} - {ranking[games[i]['team2']]}")