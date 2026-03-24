import tkinter as tk
from tkinter import ttk

from UI.registry import PAGES

class NavigationManager:
    def __init__(self):
        self.current = None
        self.history = []

    def navigate(self, page_name):
        if self.current:
            self.history.append(self.current)
        self.current = page_name

    def back(self):
        if not self.history:
            return None
        self.current = self.history.pop()
        return self.current

class Auction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.nav = NavigationManager()

        container = ttk.Frame(self)
        container.pack(fill = "both", expand = True)

        self.frames = {}
        self.frameStack = []

        for PageClass in PAGES:
            page = PageClass(container, self, self.nav)
            self.frames[PageClass.__name__] = page
            page.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame("HomePage")

    def showFrame(self, destPageName):
        self.nav.navigate(destPageName)
        frame = self.frames[destPageName]
        frame.tkraise()

    def goBack(self):
        prev = self.nav.back()
        self.nav.current = prev
        self.frames[prev].tkraise()