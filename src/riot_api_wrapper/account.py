import requests 
from src.utils.utils import convert_to_url_format
from src.riot_api_wrapper.matches import Matches

class Account():
    def __init__(self, engine, game_name, tag_line):
        self.engine = engine
        self.game_name = game_name
        self.tag_line = tag_line
        self.puuid = self._get_puuid()

    def _get_account_by_riot_id(self):
        game_name_formatted = convert_to_url_format(self.game_name)
        tag_line_formatted = convert_to_url_format(self.tag_line)
        url = "https://{}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{}/{}".format(self.engine.get_region(), game_name_formatted, tag_line_formatted)
        headers = self.engine.get_default_headers()
        response = requests.get(url, headers=headers)
        return response
    
    def _get_puuid(self):
        response_json = self._get_account_by_riot_id().json()
        return response_json['puuid']

    def get_recent_matches(self, count, startepoch=0):
        url = "https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?startTime={}&start=0&count={}".format(self.engine.get_region(), self.puuid, startepoch, count)
        headers = self.engine.get_default_headers()
        matches_ids = requests.get(url, headers=headers).json()
        matches = Matches(self.engine, matches_ids)
        return matches
    
