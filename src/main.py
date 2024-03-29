import sys
import time
import json
sys.path.append('.')

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account
from src.overlay.overlay import Overlay
from src.overlay.login import Login

def refresh(account : Account, overlay : Overlay, launch_time):
    puuid = account.puuid

    matches = account.get_recent_matches(count=count, startepoch=launch_time)
    already_displayed_matches_ids = overlay.get_already_displayed_matches_ids()

    new_matches = matches.remove_matches_ids(already_displayed_matches_ids)

    victory_booleans = new_matches.get_victory_booleans_list(puuid)
    champions_played = new_matches.get_champions_played(puuid)
    
    new_vignettes = [champion.get_processed_vignette2(victory_boolean) for champion, victory_boolean in zip(champions_played, victory_booleans)]

    overlay.display_new_matches(new_vignettes)
    overlay.append_new_matches(new_matches.get_matches_ids())

    overlay.root.after(30000, lambda : refresh(account, overlay, launch_time))

if __name__=='__main__':

    region = 'europe'
    game_name = 'nina simone'
    tag_line = 'euw'
    count = 20
    refresh_interval = 5000

    overlay = Overlay()
    overlay.withdraw()

    login_window = Login(overlay)
    launch_time = int(time.time())
    engine = Engine(region)
    account = Account(engine, game_name, tag_line)

    refresh(account, overlay, launch_time)

    print('Running NOW')
    overlay.mainloop()
   


    


    
