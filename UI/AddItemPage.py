import tkinter as tk
from tkinter import ttk

class AddItemPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        label = ttk.Label(self, text="Add Item", font=("Arial", 16))
        id_label = ttk.Label(self, text="ID:")
        id_entry = ttk.Entry(self)
        name_label = ttk.Label(self, text="Name:")
        name_entry = ttk.Entry(self)
        price_label = ttk.Label(self, text="Starting Price:")
        price_entry = ttk.Entry(self)
        donor_label = ttk.Label(self, text="Donor:")
        donor_entry = ttk.Entry(self)
        add_button = ttk.Button(self, text="Add Item", command=lambda: parent.master.show_frame("UnfinishedPage"))
        back_button = ttk.Button(self, text="Back to Items", command=lambda: parent.master.go_back())

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)

        label       .grid(row=0, column=0, columnspan=8, padx=10, pady=10)
        id_label     .grid(row=1, column=0, padx=10, pady=10, sticky="e")
        id_entry     .grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        name_label   .grid(row=1, column=2, padx=10, pady=10, sticky="e")
        name_entry   .grid(row=1, column=3, padx=10, pady=10, sticky="ew")
        price_label  .grid(row=1, column=4, padx=10, pady=10, sticky="e")
        price_entry  .grid(row=1, column=5, padx=10, pady=10, sticky="ew")
        donor_label  .grid(row=1, column=6, padx=10, pady=10, sticky="e")
        donor_entry  .grid(row=1, column=7, padx=10, pady=10, sticky="ew")
        add_button   .grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        back_button  .grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky="ew")