import tkinter as tk
from tkinter import ttk

class StatsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        label = ttk.Label(self, text="Stats")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        label.grid(row=0, column=9, padx=10, pady=10, sticky="nsew")

    def refresh(self):
        pass
