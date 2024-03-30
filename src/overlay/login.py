import tkinter as tk
import time
from tkinter import Toplevel, Button, messagebox

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account

class Login(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.title('League Tatracker')
        self.geometry('300x150')
        self.parent = parent
        self.protocol('WM_DELETE_WINDOW', self.quit)

        self.background_color = "gray18"

        self.configure(background='gray18')

        self.frame = tk.Frame(self, background=self.background_color)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.game_name_label = tk.Label(self.frame, text="Game name :", background=self.background_color, fg="white", font=(13) )
        self.game_name_label.grid(row=0, column=0)

        self.game_name_entry = tk.Entry(self.frame)
        self.game_name_entry.grid(row=0, column=1)

        self.tag_line_label = tk.Label(self.frame, text="Tag line : ", background=self.background_color, fg="white", font=(13) )
        self.tag_line_label.grid(row=1, column= 0)

        self.tag_line_entry = tk.Entry(self.frame)
        self.tag_line_entry.grid(row=1, column = 1)

        self.region_label = tk.Label(self.frame, text='Region :', background=self.background_color, fg="white", font=(13) )
        self.region_label.grid(row=2, column = 0)

        self.region_entry = tk.Entry(self.frame)
        self.region_entry.grid(row=2, column = 1)

        self.button = Button(self.frame, text='Launch tracker', command=self.login, font=(15))
        self.button.grid(row=3, column = 0, columnspan = 2, sticky="EW", pady=4)

        for i in range(4):
            self.frame.rowconfigure(i, pad=4)

        for i in range(2):
            self.frame.columnconfigure(i, pad = 4)
        
    def login(self):
        game_name = self.game_name_entry.get()
        tag_line = self.tag_line_entry.get()
        region = self.region_entry.get()

        if len(game_name) == 0 or len(tag_line)==0 or len(region)==0 :
            messagebox.showerror("Login Failed", "Please provide correct credentials.")
        else :
            launch_time = int(time.time())
            engine = Engine(region)
            account = Account(engine, game_name, tag_line)
            self.destroy()

            self.parent.refresh(account, launch_time)
            print('Running NOW')
            self.parent.deiconify()