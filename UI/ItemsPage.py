import tkinter as tk
from tkinter import ttk

class ItemsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        treeviewColumns = ("ID", "Name", "Donor", "Starting Price", "Buyer", "Ending Price")

        # Create a label
        label = ttk.Label(self, text="Items", font=("Arial", 16))
        # TODO: Add add item page
        addButton = ttk.Button(self, text="Add Item", command=lambda: parent.master.showFrame("AddItemPage"))
        # TODO: Add edit item page
        editButton = ttk.Button(self, text="Edit Item", command=lambda: parent.master.showFrame("UnfinishedPage"))
        # TODO: Add delete item page
        deleteButton = ttk.Button(self, text="Delete Item", command=lambda: parent.master.showFrame("UnfinishedPage"))
        backButton = ttk.Button(self, text="Back to Home", command=lambda: parent.master.goBack())
        itemTreeview = ttk.Treeview(self, columns=treeviewColumns, show="headings")

        itemTreeview.heading("ID", text="ID")
        itemTreeview.column("ID", width=50, anchor="center")
        itemTreeview.heading("Name", text="Name")
        itemTreeview.column("Name", width=100, anchor="center")
        itemTreeview.heading("Donor", text="Donor")
        itemTreeview.column("Donor", width=100, anchor="center")
        itemTreeview.heading("Starting Price", text="Starting Price")
        itemTreeview.column("Starting Price", width=150, anchor="center")
        itemTreeview.heading("Buyer", text="Buyer")
        itemTreeview.column("Buyer", width=100, anchor="center")
        itemTreeview.heading("Ending Price", text="Ending Price")
        itemTreeview.column("Ending Price", width=150, anchor="center")

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        addButton.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        editButton.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        deleteButton.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        backButton.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        itemTreeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def updateItems(self):
        pass