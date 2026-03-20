import tkinter as tk
from tkinter import ttk

class Auction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")

        container = ttk.Frame(self)
        container.pack(fill = "both", expand = True)

        self.frames = {}

        for PageClass in (HomePage, CreateDonorPage):
            page = PageClass(container, self)
            self.frames[PageClass] = page
            page.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(StartPage)

    def showFrame(self, pageClass):
        frame = self.frames[pageClass]
        frame.tkraise()