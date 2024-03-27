import tkinter as tk
from PIL import Image, ImageTk

class Overlay:

    def __init__(self):
        self.already_displayed_matches_ids = []
        self.displayed_vignettes= []

        self.root = tk.Tk()

        self.root.geometry('1000x150')
        self.root.resizable(width=False, height=False)
        self.root.wm_attributes('-transparentcolor', self.root['bg'])   

        self.root.attributes('-topmost', True)

        self.root.overrideredirect(True)

        #self.recent_games_frame = tk.Frame(self.root, height = 100, width=500)
        #self.recent_games_frame.place(relx=.5, rely=.5, anchor= 'center')

        #for i in range (5):
        #    self.recent_games_frame.columnconfigure(i, weight = 1)

    def append_new_matches(self, new_matches_ids): 
        self.already_displayed_matches_ids.extend(new_matches_ids)
        
    def display_new_matches(self, new_vignettes):
        new_vignettes = list(reversed(new_vignettes))
        for i, vignette in enumerate(new_vignettes) : 
            img = ImageTk.PhotoImage(vignette)
            label = tk.Label(self.root, image = img)
            label.grid(row = 0, column = len(self.already_displayed_matches_ids) + i)
            self.displayed_vignettes.append(img)

    def get_already_displayed_matches_ids(self):
        return self.already_displayed_matches_ids
    
    def mainloop(self):
        self.root.mainloop()