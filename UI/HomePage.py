import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        tab_control = ttk.Notebook(self)
        tab_control.grid(row=0, column=0, sticky="nsew")
        tab_control.add(self.controller.frames["StatsPage"], text="Stats")
        tab_control.add(self.controller.frames["DonorsPage"], text="Donors")
        tab_control.add(self.controller.frames["ItemsPage"], text="Items")
        tab_control.add(self.controller.frames["BuyersPage"], text="Buyers")
        tab_control.add(self.controller.frames["UnfinishedPage"], text="Receipts")
        # label = ttk.Label(self, text="Home Page", font=("Arial", 16))
        # donors_button = ttk.Button(self, text="Donors", command=lambda: parent.master.show_frame("DonorsPage"))
        # items_button = ttk.Button(self, text="Items", command=lambda: parent.master.show_frame("ItemsPage"))
        # bidders_button = ttk.Button(self, text="Buyers", command=lambda: parent.master.show_frame("BuyersPage"))
        # receipts_button = ttk.Button(self, text="Receipts", command=lambda: parent.master.show_frame("UnfinishedPage"))

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=2)
        # self.grid_rowconfigure(2, weight=2)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)

        # label               .grid(row=0, column=0, columnspan=2,    padx=10,    pady=10, sticky="nsew")
        # donors_button       .grid(row=1, column=0,                  padx=10,    pady=10, sticky="nsew")
        # items_button        .grid(row=1, column=1,                  padx=10,    pady=10, sticky="nsew")
        # bidders_button      .grid(row=2, column=0,                  padx=10,    pady=10, sticky="nsew")
        # receipts_button     .grid(row=2, column=1,                  padx=10,    pady=10, sticky="nsew")

    def refresh(self):
        pass
