import tkinter as tk
from tkinter import ttk

from globals import ObjectType
from UI.ObjectsPage import ObjectsPage
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
    def __init__(self, all_data):
        super().__init__()
        self.title("App")
        self.nav = NavigationManager()
        self.all_data = all_data

        container = ttk.Frame(self)
        container.pack(fill = "both", expand = True)

        self.frames = {}
        self.frameStack = []

        for PageClass in PAGES:
            # TODO: Because I can access show_frame and go_back through controller, investigate whether the parent parameter is necessary
            page = PageClass(container, self, self.nav)
            self.frames[PageClass.__name__] = page
            page.grid(row = 0, column = 0, sticky = "nsew")

        page = ObjectsPage(container, self, ObjectType.DONOR, self.nav)
        self.frames["DonorsPage"] = page
        page.grid(row = 0, column = 0, sticky = "nsew")

        page = ObjectsPage(container, self, ObjectType.ITEM, self.nav)
        self.frames["ItemsPage"] = page
        page.grid(row = 0, column = 0, sticky = "nsew")

        page = ObjectsPage(container, self, ObjectType.BUYER, self.nav)
        self.frames["BuyersPage"] = page
        page.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("HomePage")

    def show_frame(self, destPageName):
        self.nav.navigate(destPageName)
        frame = self.frames[destPageName]
        frame.refresh()
        frame.tkraise()

    def go_back(self):
        prev = self.nav.back()
        self.nav.current = prev
        self.frames[prev].tkraise()
        self.frames[prev].refresh()

    def commit_action(self, object_type, treeview):
        pass
