import tkinter as tk
from PIL import ImageTk

class Overlay(tk.Tk):
    VIGNETTES_PER_ROW = 8

    def __init__(self):
        super().__init__()
        self.already_displayed_matches_ids = []
        self.displayed_vignettes= [] #anti-garbagecollector

        self.resizable(width=False, height=False)
        self.wm_attributes('-transparentcolor', self['bg'])   

        self.attributes('-topmost', True)

        self.overrideredirect(True)
        
    def _display_new_matches(self, new_vignettes):
        new_vignettes = list(reversed(new_vignettes))
        for i, vignette in enumerate(new_vignettes) : 
            row_index = (len(self.already_displayed_matches_ids) + i) // self.VIGNETTES_PER_ROW
            column_index = (len(self.already_displayed_matches_ids) + i) % self.VIGNETTES_PER_ROW
            img = ImageTk.PhotoImage(vignette)
            label = tk.Label(self, image = img)
            label.grid(row = row_index, column = column_index)
            self.displayed_vignettes.append(img) #anti-garbagecollector

    def refresh(self, account, launch_time):
        puuid = account.puuid

        matches = account.get_recent_matches(count=20, startepoch=launch_time)

        new_matches = matches.remove_matches_ids(self.already_displayed_matches_ids)

        victory_booleans = new_matches.get_victory_booleans_list(puuid)
        champions_played = new_matches.get_champions_played(puuid)
        
        new_vignettes = [champion.get_processed_vignette2(victory_boolean) for champion, victory_boolean in zip(champions_played, victory_booleans)]

        self._display_new_matches(new_vignettes)

        self.already_displayed_matches_ids.extend(new_matches.get_matches_ids())

        self.after(30000, lambda : self.refresh(account, launch_time))