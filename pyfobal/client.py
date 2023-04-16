import requests
from .types import League

class Client:
    def __init__(self, api_key, api_version='v1'):
        self.base_url = f'https://api.example.com/{api_version}'
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def _make_request(self, endpoint):
        url = f'{self.base_url}{endpoint}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _process_data(self, data, entity_class):
        return [entity_class(item) for item in data]



    # API Endpoints
    def get_leagues(self):
        endpoint = '/leagues'
        data = self._make_request(endpoint)
        return self._process_data(data, League)

    def get_league_by_id(self, league_id):
        endpoint = f'/leagues/{league_id}'
        data = self._make_request(endpoint)
        return self._process_data(data, League)
