import tkinter as tk
from tkinter import ttk

class AddItemPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        label = ttk.Label(self, text="Add Item", font=("Arial", 16))
        idLabel = ttk.Label(self, text="ID:")
        idEntry = ttk.Entry(self)
        nameLabel = ttk.Label(self, text="Name:")
        nameEntry = ttk.Entry(self)
        priceLabel = ttk.Label(self, text="Starting Price:")
        priceEntry = ttk.Entry(self)
        donorLabel = ttk.Label(self, text="Donor:")
        donorEntry = ttk.Entry(self)
        addButton = ttk.Button(self, text="Add Item", command=lambda: parent.master.showFrame("UnfinishedPage"))
        backButton = ttk.Button(self, text="Back to Items", command=lambda: parent.master.goBack())

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
        idLabel     .grid(row=1, column=0, padx=10, pady=10, sticky="e")
        idEntry     .grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        nameLabel   .grid(row=1, column=2, padx=10, pady=10, sticky="e")
        nameEntry   .grid(row=1, column=3, padx=10, pady=10, sticky="ew")
        priceLabel  .grid(row=1, column=4, padx=10, pady=10, sticky="e")
        priceEntry  .grid(row=1, column=5, padx=10, pady=10, sticky="ew")
        donorLabel  .grid(row=1, column=6, padx=10, pady=10, sticky="e")
        donorEntry  .grid(row=1, column=7, padx=10, pady=10, sticky="ew")
        addButton   .grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        backButton  .grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky="ew")