import os
import sys
import time
sys.path.append('.')

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account
from src.riot_api_wrapper.matches import Matches
from src.riot_api_wrapper.champion import Champion

if __name__=='__main__':
    region = "europe"
    game_name = "nina simone"
    tag_line = "euw"
    count = 20

    launch_time = int(time.time())

    engine = Engine(region)
    account = Account(engine, game_name, tag_line)
    puuid = account.get_puuid()
    matches_ids = account.get_recent_matches_ids(count=count, startepoch=launch_time-10000)

    matches = Matches(engine, matches_ids)
    victory_booleans = matches.get_victory_booleans_list(puuid)
    champions_played = matches.get_champions_played(puuid)
    
    vignettes = [champion.get_processed_vignette(victory_boolean) for champion, victory_boolean in zip(champions_played, victory_booleans)]

    

    


    
