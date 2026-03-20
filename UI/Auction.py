import tkinter as tk
from tkinter import ttk

from UI.registry import PAGES

class Auction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")

        container = ttk.Frame(self)
        container.pack(fill = "both", expand = True)

        self.frames = {}

        for PageClass in PAGES:
            page = PageClass(container, self)
            self.frames[PageClass.__name__] = page
            page.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame("HomePage")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()