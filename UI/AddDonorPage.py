import tkinter as tk
from tkinter import ttk

class AddDonorPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        # TODO: Make a submit button that allows submission if all fields are properly populated
        label = ttk.Label(self, text="Add Donor")
        ID_label = ttk.Label(self, text="ID")
        name_label = ttk.Label(self, text="Name")
        address_label = ttk.Label(self, text="Address")
        ID_entry = ttk.Entry(self)
        name_entry = ttk.Entry(self)
        address_entry = ttk.Entry(self)
        back_button = ttk.Button(self, text="Back", command= lambda: parent.master.go_back())

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        ID_label.grid(row=1, column=0, padx=10, sticky="ew")
        name_label.grid(row=1, column=1, padx=10, sticky="ew")
        address_label.grid(row=1, column=2, padx=10, sticky="ew")
        ID_entry.grid(row=2, column=0, padx=10, sticky="ew")
        name_entry.grid(row=2, column=1, padx=10, sticky="ew")
        address_entry.grid(row=2, column=2, padx=10, sticky="ew")
        back_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)