import tkinter as tk
from PIL import ImageTk

class Overlay:

    VIGNETTES_PER_ROW = 8

    def __init__(self):
        self.already_displayed_matches_ids = []
        self.displayed_vignettes= [] #anti-garbagecollector

        self.root = tk.Tk()

        self.root.resizable(width=False, height=False)
        self.root.wm_attributes('-transparentcolor', self.root['bg'])   

        self.root.attributes('-topmost', True)

        self.root.overrideredirect(True)

    def append_new_matches(self, new_matches_ids): 
        self.already_displayed_matches_ids.extend(new_matches_ids)
        
    def display_new_matches(self, new_vignettes):
        new_vignettes = list(reversed(new_vignettes))
        for i, vignette in enumerate(new_vignettes) : 
            row_index = (len(self.already_displayed_matches_ids) + i) // self.VIGNETTES_PER_ROW
            column_index = (len(self.already_displayed_matches_ids) + i) % self.VIGNETTES_PER_ROW
            img = ImageTk.PhotoImage(vignette)
            label = tk.Label(self.root, image = img)
            label.grid(row = row_index, column = column_index)
            self.displayed_vignettes.append(img) #anti-garbagecollector

    def get_already_displayed_matches_ids(self):
        return self.already_displayed_matches_ids
    
    def withdraw(self):
        self.root.withdraw()

    def deiconify(self):
        self.root.deiconify()

    def mainloop(self):
        self.root.mainloop()