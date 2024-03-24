import json
import requests 

from src.riot_api_wrapper.champion import Champion

class Match():
    def __init__(self, engine, match_id):
        self.engine = engine
        self.match_id = match_id
        self.game_info = self._get_game_info()

    def get_match_id(self):
        return self.match_id
    
    def _get_game_info(self):
        url = "https://{}.api.riotgames.com/lol/match/v5/matches/{}".format(self.engine.get_region(), self.match_id)
        headers = self.engine.get_default_headers()
        response = requests.get(url, headers=headers)
        return response.json()
    
    def get_participant(self, puuid):
        participants = self.game_info['info']['participants']
        
        for x in participants : 
            if x['puuid'] == puuid:
                participant = x
                break
        try : 
            assert participant is not None
        except : 
            raise Exception("Player requested is not part of this match.")
        
        return participant

    def get_champion_played(self, puuid):
        participant = self.get_participant(puuid)
        return Champion(self.engine, participant['championId'])


    def get_victory_boolean(self, puuid):
        participant = self.get_participant(puuid)
        return participant['win']
