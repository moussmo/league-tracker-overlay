import tkinter as tk


class Overlay:

    def __init__(self):
        self.already_displayed_matches_ids = []

        self.root = tk.TK()

        recent_games_frame = tk.Frame(self.root, height=5, background='')
        recent_games_frame.pack()

    def append_new_matches(self, new_matches_ids): 
        self.already_displayed_matches_ids.append(new_matches_ids)
        
    def display_new_matches(self, new_vignettes):
        pass

    def get_already_displayed_matches_ids(self):
        return self.already_displayed_matches_ids
    
    def mainloop(self):
        self.root.mainloop()