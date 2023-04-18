

from pyfobal.fobal_types.Player import Player
from pyfobal.fobal_types.Team import Team


class Fixture:
    def __init__(self, client, data : dict):  
        self.client = client

        self.fixture_id = data.get('fixture_id')
        self.season = data.get('season')
        self.nation = data.get('nation')
        self.league = data.get('league')
        self.league_id = data.get('league_id')
        self.matchday = data.get('matchday')
        self.date = data.get('date')
        self.home = data.get('home')
        self.away = data.get('away')
        self.home_id = data.get('home_id')
        self.away_id = data.get('away_id')
        self.home_score = data.get('home_score')
        self.away_score = data.get('away_score')
        self.home_score_1T = data.get('home_score_1T')
        self.away_score_1T = data.get('away_score_1T')
        self.home_score_2T = data.get('home_score_2T')
        self.away_score_2T = data.get('away_score_2T')
        self.stadium = data.get('stadium')
        self.referee = data.get('referee')
        self.is_terminated = data.get('is_terminated')
        self.diretta_link = data.get('diretta_link')
        self.transfermarkt_id = data.get('transfermarkt_id')
        self.transfermarkt_url = data.get('transfermarkt_url')
        self.diretta_id = data.get('diretta_id')
        self.direttait_url = data.get('direttait_url')
        self.fbref_id = data.get('fbref_id')
        self.fbref_url = data.get('fbref_url')

    # To dictionary
    def to_dict(self) -> dict:
        return {
            'fixture_id': self.fixture_id,
            'season': self.season,
            'nation': self.nation,
            'league': self.league,
            'league_id': self.league_id,
            'matchday': self.matchday,
            'date': self.date,
            'home': self.home,
            'away': self.away,
            'home_id': self.home_id,
            'away_id': self.away_id,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'home_score_1T': self.home_score_1T,
            'away_score_1T': self.away_score_1T,
            'home_score_2T': self.home_score_2T,
            'away_score_2T': self.away_score_2T,
            'stadium': self.stadium,
            'referee': self.referee,
            'is_terminated': self.is_terminated,
            'diretta_link': self.diretta_link,
            'transfermarkt': self.transfermarkt_url,
            'transfermarkt_id': self.transfermarkt_id,
            'diretta': self.direttait_url,
            'diretta_id': self.diretta_id,
            'fbref': self.fbref_url,
            'fbref_id': self.fbref_id,
        }
    
    def get_teams(self):
        data = self.client._request("GET", f"/fixtures/{self.fixture_id}/teams")
        return self.client._process_data(data, Team)

    def get_players(self) -> list[list]:
        '''
        Get the players of the fixture.

        Returns [home_players, away_players]: 
            [[Player, Player, ...], [Player, Player, ...]]
        '''

        data = self.client._request("GET", f"/fixtures/{self.fixture_id}/players")
        return [self.client._process_data(data[0], Player), self.client._process_data(data[1], Player) ]