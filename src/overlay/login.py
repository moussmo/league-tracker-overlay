import tkinter as tk
import time
from tkinter import Toplevel, Button, messagebox

from src.riot_api_wrapper.engine import Engine
from src.riot_api_wrapper.account import Account

class Login(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.title('Login')
        self.geometry('500x300')
        self.parent = parent
        #self.protocol('WM_DELETE_WINDOW', root.quit)
        self.game_name_label = tk.Label(self, text="Game name :")
        self.game_name_label.pack()

        self.game_name_entry = tk.Entry(self)
        self.game_name_entry.pack()

        self.tag_line_label = tk.Label(self, text="Tag line : ")
        self.tag_line_label.pack()

        self.tag_line_entry = tk.Entry(self)
        self.tag_line_entry.pack()

        self.region_label = tk.Label(self, text='Region :')
        self.region_label.pack()

        self.region_entry = tk.Entry(self)
        self.region_entry.pack()

        self.button = Button(self, text='Login', command=self.login)
        self.button.pack()
        
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
            self.parent.refresh(account, launch_time)
            self.destroy()
            self.parent.deiconify()