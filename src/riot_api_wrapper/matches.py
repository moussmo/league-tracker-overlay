import os
import requests 
from src.riot_api_wrapper.match import Match
from src.riot_api_wrapper.champion import Champion

class Matches():
    def __init__(self, engine, matches_ids):
        self.engine = engine
        self.matches_ids = matches_ids
        self.matches = [Match(self.engine, match_id) for match_id in matches_ids]

    def get_victory_booleans_list(self, puuid):
        return [match.get_victory_boolean(puuid) for match in self.matches]
    
    def get_champions_played(self, puuid):
        return [match.get_champion_played(puuid) for match in self.matches]