

class Team:
    def __init__(self, client, data : dict):  
        self.client = client
  
        self.team_id = data.get('team_id')
        self.name = data.get('name')
        self.visual_name = data.get('visual_name')
        self.tag = data.get('tag')
        self.league_id = data.get('league_id')
        self.nation = data.get('nation')
        self.city = data.get('city')
        self.stadium = data.get('stadium')
        self.stadium_address = data.get('stadium_address')
        self.seats = data.get('seats')
        self.squad_size = data.get('squad_size')
        self.logo = data.get('logo')
        self.transfermarkt_id = data.get('transfermarkt_id')
        self.diretta_id = data.get('diretta_id')
        self.fbref_id = data.get('fbref_id') 
        self.transfermarkt_url = data.get('transfermarkt_url')
        self.direttait_url = data.get('direttait_url')
        self.fbref_url = data.get('fbref_url')
 
    # Get players
    def get_players(self):
        return self.client.get_players_by_team_id(self.team_id)
 
    # To dictionary
    def to_dict(self) -> dict:
        return {
            'team_id': self.team_id,
            'name': self.name,
            'visual_name': self.visual_name,
            'tag': self.tag,
            'league_id': self.league_id,
            'nation': self.nation,
            'city': self.city,
            'stadium': self.stadium,
            'stadium_address': self.stadium_address,
            'seats': self.seats,
            'squad_size': self.squad_size,
            'logo': self.logo,
            'transfermarkt': self.transfermarkt_url,
            'transfermarkt_id': self.transfermarkt_id,
            'diretta': self.direttait_url,
            'diretta_id': self.diretta_id,
            'fbref': self.fbref_url,
            'fbref_id': self.fbref_id, 
        }
        
 
 
    