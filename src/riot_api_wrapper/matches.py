import os
import requests 
from src.riot_api_wrapper.match import Match
from src.riot_api_wrapper.champion import Champion

class Matches():
    def __init__(self, engine, matches_ids):
        self.engine = engine
        self.matches_ids = matches_ids
        self.matches = [Match(self.engine, match_id) for match_id in matches_ids]

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        x = self.matches[self.index]
        self.index +=1
        return x 
    
    def get_matches_ids(self):
        return self.matches_ids
    
    def get_victory_booleans_list(self, puuid):
        return [match.get_victory_boolean(puuid) for match in self.matches]
    
    def get_champions_played(self, puuid):
        return [match.get_champion_played(puuid) for match in self.matches]
    
    def remove_matches_ids(self, matches_ids_to_remove):
        matches_ids = [id for id in self.matches_ids if id not in matches_ids_to_remove]
        return Matches(self.engine, matches_ids)