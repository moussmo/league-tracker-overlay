import sys

sys.path.append('.')

from src.overlay.overlay import Overlay
from src.overlay.login import Login

if __name__=='__main__':
    overlay = Overlay()
    overlay.withdraw()

    login_window = Login(overlay)

    overlay.mainloop()
   


    


    
