import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']

    def players_points(self):
        return self.assists + self.goals
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists} = {self.players_points()}"

class PlayerReader:
    def __init__(self,url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players
    
class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self,nationality):
        players_by_nationality = []
        self.nationality = nationality

        for player in self.players:
            if player.nationality == self.nationality:
                players_by_nationality.append(player)

        return sorted(players_by_nationality, key=Player.players_points, reverse=True)