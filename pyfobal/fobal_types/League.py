
from pyfobal.fobal_types.Player import Player
from pyfobal.fobal_types.Team import Team


class League:
    def __init__(self, client, data : dict):  
        self.client = client
        self.league_id = data.get('league_id')
        self.name = data.get('name')
        self.nation = data.get('nation')
        self.league_level = data.get('league_level')
        self.n_teams = data.get('squad_size')  
        self.logo = data.get('logo')
        self.transfermarkt_id = data.get('transfermarkt_id')
        self.diretta_id = data.get('diretta_id')
        self.fbref_id = data.get('fbref_id')
        self.transfermarkt_url = data.get('transfermarkt_url')
        self.direttait_url = data.get('direttait_url')
        self.fbref_url = data.get('fbref_url')  
        
    def to_dict(self):
        return {
            'league_id': self.league_id,
            'name': self.name,
            'nation': self.nation,
            'league_level': self.league_level,
            'n_teams': self.n_teams,
            'logo': self.logo,
            'transfermarkt_id': self.transfermarkt_id,
            'transfermarkt_url': self.transfermarkt_url,
            'diretta_id': self.diretta_id,
            'diretta_url': self.direttait_url,
            'fbref_id': self.fbref_id,
            'fbref_url': self.fbref_url
        }

    def get_teams(self):
        data = self.client._request("GET", f"/leagues/{self.league_id}/teams")
        return self.client._process_data(data, Team)

    def get_players(self):
        data = self.client._request("GET", f"/leagues/{self.league_id}/players")
        return self.client._process_data(data, Player)