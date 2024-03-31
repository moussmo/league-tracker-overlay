import tkinter as tk
import time
from tkinter import Toplevel, Button, messagebox, ttk

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account

class Login(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.title('League Tatracker')

        window_width = 400
        window_height = 150
        x_coordinates, y_coordinates = self._calculate_center_screen_coordinates(window_width=window_width, window_height=window_height)
        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_coordinates, y_coordinates))

        self.parent = parent
        self.protocol('WM_DELETE_WINDOW', self.quit)

        self.background_color = "gray18"

        self.configure(background='gray18')

        self.frame = tk.Frame(self, background=self.background_color)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.game_name_label = tk.Label(self.frame, text="Game name :", background=self.background_color, fg="white", font=(13) )
        self.game_name_label.grid(row=0, column=0)
        self.game_name_entry = tk.Entry(self.frame, font=13)
        self.game_name_entry.grid(row=0, column=1)

        self.tag_line_label = tk.Label(self.frame, text="Tag line : ", background=self.background_color, fg="white", font=(13) )
        self.tag_line_label.grid(row=1, column= 0)
        self.tag_line_entry = tk.Entry(self.frame, font=13)
        self.tag_line_entry.grid(row=1, column = 1)

        self.regions_list = ["Europe", "Americas", "Asia"]
        self.region_label = tk.Label(self.frame, text='Region :', background=self.background_color, fg="white", font=(13))
        self.region_label.grid(row=2, column = 0)
        self.region_entry = ttk.Combobox(self.frame, values=self.regions_list, font=13)
        self.region_entry.grid(row=2, column = 1)
        self.region_entry['state'] = 'readonly'
        self.region_entry.set(self.regions_list[0])

        self.button = Button(self.frame, text='Launch tracker', command=self.login, font=(15))
        self.button.grid(row=3, column = 0, columnspan = 2, sticky="EW", pady=4)

        for i in range(4):
            self.frame.rowconfigure(i, pad=4)

        for i in range(2):
            self.frame.columnconfigure(i, pad = 4)
    
    def _calculate_center_screen_coordinates(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        return x_coordinate, y_coordinate
    
    def login(self):
        game_name = self.game_name_entry.get().strip()
        tag_line = self.tag_line_entry.get().strip()
        region = self.region_entry.get().strip().lower()

        if len(game_name) == 0 or len(tag_line)==0 or len(region)==0 :
            messagebox.showerror("Login Failed", "Please provide correct credentials.")
        else :
            try : 
                launch_time = int(time.time())
                engine = Engine(region)
                account = Account(engine, game_name, tag_line)
                self.frame.destroy()

                self.parent.refresh(account, launch_time)
                self.parent.deiconify()
                
                self.label = tk.Label(self, text="Tracker currently active", font=15, bg=self.background_color, fg= 'white')
                self.label.place(relx=0.5, rely=0.5, anchor='center')
            except:
                messagebox.showerror("Error accountered when accessing the server.")
