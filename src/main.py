import sys

import json
sys.path.append('.')

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account
from src.overlay.overlay import Overlay
from src.overlay.login import Login

if __name__=='__main__':
    overlay = Overlay()
    overlay.withdraw()

    login_window = Login(overlay)

    print('Running NOW')
    overlay.mainloop()
   


    


    
