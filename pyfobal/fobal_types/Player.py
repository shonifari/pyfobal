

class Player:
    
    def __init__(self,client, data: dict):
        self.client = client
        
        self.player_id = data.get('player_id')
        self.name = data.get('name')
        self.team_id = data.get('team_id')
        self.league_id = data.get('league_id')
        self.nation = data.get('nation')
        self.number = data.get('number')
        self.dob = data.get('dob')
        self.height = data.get('height')
        self.position = data.get('position')
        self.foot = data.get('foot')
        self.status = data.get('status')
        self.visual_name = data.get('visual_name')
        self.fantacalcio_id = data.get('fantacalcio_id')
        self.fanta_position = data.get('fanta_position')
        self.img = data.get('img')
        self.transfermarkt_id = data.get('transfermarkt_id')
        self.diretta_id = data.get('diretta_id')
        self.fbref_id = data.get('fbref_id')
        self.position_tag = data.get('position_tag')
        self.transfermarkt_url = data.get('transfermarkt_url')
        self.diretta_url = data.get('diretta_url')
        self.age = data.get('age')
         

    
    def to_dict(self):
        return {
        "player_id" : self.player_id,
        "name" : self.name,
        "team_id" : self.team_id,
        "league_id" : self.league_id,
        "nation" : self.nation,
        "number" : self.number,
        "dob" : self.dob,
        "height" : self.height,
        "position" : self.position,
        "foot" : self.foot,
        "status" : self.status,
        "visual_name" : self.visual_name,
        "fantacalcio_id" : self.fantacalcio_id,
        "fanta_position" : self.fanta_position,
        "img" : self.img,
        "transfermarkt_id" : self.transfermarkt_id,
        "diretta_id" : self.diretta_id,
        "fbref_id" : self.fbref_id,
        "position_tag" : self.position_tag,
        "transfermarkt_url" : self.transfermarkt_url,
        "diretta_url" : self.diretta_url,
        "age" : self.age
        }

if __name__ == '__main__':
 pass