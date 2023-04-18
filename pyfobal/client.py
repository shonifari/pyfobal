import requests


from .fobal_types import League, Team , Player, Fixture

class Client:
    def __init__(self, api_key, api_version='v1'):
        self.base_url = f'http://132.145.58.62:8000/{api_version}'
        self.base_url = f'http://132.145.58.62:8000/data'
        self.base_url = f'http://127.0.0.1:5000/data'
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def _request(self, method, endpoint, params=None):
        url = f'{self.base_url}{endpoint}'
        response = requests.request(method, url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _process_data(self, data, entity_class):
        return [entity_class(self,item) for item in data]






    # API Endpoints
    def get_leagues(self, league_id=None, name=None, nation=None, level=None):
        params = {
            "id": league_id,
            "name": name,
            "nation": nation,
            "level": level
        }
        data = self._request("GET", "/leagues", params=params)
        return self._process_data(data, League)

    
    def get_league(self, league_id=None, name=None):
        params = {
            "id": league_id,
            "name": name
        }
        data = self._request("GET", "/leagues", params=params)
        result = self._process_data(data, League)
        return result[0] if len(result) > 0 else None        

    
    

        
    ############################## 

    def get_fixtures(self,
                    fixture_id=None,
                    season = None, 
                    nation = None, 
                    league = None, 
                    league_id = None, 
                    matchday = None, 
                    date = None, 
                    home = None, 
                    away = None, 
                    home_id = None, 
                    away_id = None, 
                    is_terminated = None
                    ):
        params = {
            "fixture_id": fixture_id,
            "season": season,
            "nation": nation,
            "league": league,
            "league_id": league_id,
            "matchday": matchday,
            "date": date,
            "home": home,
            "away": away,
            "home_id": home_id,
            "away_id": away_id,
            "is_terminated": is_terminated,
        }
        data = self._request("GET", "/fixtures", params=params)
        return self._process_data(data, Fixture)

    def get_fixture(self,
                    fixture_id=None,
                    season = None,
                    date = None, 
                    home = None, 
                    away = None, 
                    home_id = None, 
                    away_id = None, 
                    is_terminated = None
                    ):
        params = {
            "fixture_id": fixture_id,
            "season": season,
            "date": date,
            "home": home,
            "away": away,
            "home_id": home_id,
            "away_id": away_id,
            "is_terminated": is_terminated,
        }
        data = self._request("GET", "/fixtures", params=params)
        result = self._process_data(data, Fixture)
        return result[0] if len(result) > 0 else None    



    ############################## 

    def get_teams(self, team_id=None, name=None, tag=None, nation=None):
        params = {
            "id": team_id,
            "name": name,
            "tag": tag,
            "nation": nation
        }
        data = self._request("GET", "/teams", params=params)
        return self._process_data(data, Team)
        
    def get_team(self, team_id=None, name=None, tag=None):
        params = {
            "id": team_id,
            "name": name,
            "tag": tag,
        }
        data = self._request("GET", "/teams", params=params)
        result = self._process_data(data, Team)
        return result[0] if len(result) > 0 else None        
 
        

    
        
        
 

    ############################## 
  
    def get_players(self,id=None, name=None, team_id=None, league_id=None, nation=None, position=None, position_tag=None, fanta_position=None):
        params = {
            "id": id,
            "name": name,
            "team_id": team_id,
            "league_id": league_id,
            "nation": nation,
            "position": position,
            "position_tag": position_tag,
            "fanta_position": fanta_position
        }
            
        data = self._request("GET", "/players", params=params)
        return self._process_data(data, Player)
        


    def get_player(self,id=None, name=None, team_id=None, league_id=None, nation=None, position=None, position_tag=None, fanta_position=None):
        params = {
            "id": id,
            "name": name,
            "team_id": team_id,
            "league_id": league_id,
            "nation": nation,
            "position": position,
            "position_tag": position_tag,
            "fanta_position": fanta_position
        }
            
        data = self._request("GET", "/players", params=params)
        result = self._process_data(data, Player)
        return result[0] if len(result) > 0 else None        
 
        

    
        