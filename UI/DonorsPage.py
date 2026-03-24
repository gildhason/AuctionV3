import tkinter as tk
from tkinter import ttk

class DonorsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        treeviewColumns = ("ID", "Name", "Address", "Items")

        # Create a label
        label = ttk.Label(self, text="Donors", font=("Arial", 16))
        # TODO: Add add donor page
        addButton = ttk.Button(self, text="Add Donor", command=lambda: parent.master.showFrame("UnfinishedPage"))
        # TODO: Add edit donor page
        editButton = ttk.Button(self, text="Edit Donor", command=lambda: parent.master.showFrame("UnfinishedPage"))
        # TODO: Add delete donor page
        deleteButton = ttk.Button(self, text="Delete Donor", command=lambda: parent.master.showFrame("UnfinishedPage"))
        backButton = ttk.Button(self, text="Back to Home", command=lambda: parent.master.goBack())
        donorTreeview = ttk.Treeview(self, columns=treeviewColumns, show="headings")

        donorTreeview.heading("ID", text="ID")
        donorTreeview.column("ID", width=50, anchor="center")
        donorTreeview.heading("Name", text="Name")
        donorTreeview.column("Name", width=100, anchor="center")
        donorTreeview.heading("Address", text="Address")
        donorTreeview.column("Address", width=150, anchor="center")
        donorTreeview.heading("Items", text="Items Donated")
        donorTreeview.column("Items", width=100, anchor="center")

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
        donorTreeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def updateDonors(self):
        pass