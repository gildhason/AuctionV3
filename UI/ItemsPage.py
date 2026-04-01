import tkinter as tk
from tkinter import ttk

class ItemsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        treeview_columns = ("ID", "Name", "Donor", "Starting Price", "Buyer", "Ending Price")

        # Create a label
        label = ttk.Label(self, text="Items", font=("Arial", 16))
        # TODO: Add add item page
        add_button = ttk.Button(self, text="Add Item", command=lambda: parent.master.show_frame("AddItemPage"))
        # TODO: Add edit item page
        edit_button = ttk.Button(self, text="Edit Item", command=lambda: parent.master.show_frame("UnfinishedPage"))
        # TODO: Add delete item page
        delete_button = ttk.Button(self, text="Delete Item", command=lambda: parent.master.show_frame("UnfinishedPage"))
        back_button = ttk.Button(self, text="Back to Home", command=lambda: parent.master.go_back())
        item_treeview = ttk.Treeview(self, columns=treeview_columns, show="headings")

        item_treeview.heading("ID", text="ID")
        item_treeview.column("ID", width=50, anchor="center")
        item_treeview.heading("Name", text="Name")
        item_treeview.column("Name", width=100, anchor="center")
        item_treeview.heading("Donor", text="Donor")
        item_treeview.column("Donor", width=100, anchor="center")
        item_treeview.heading("Starting Price", text="Starting Price")
        item_treeview.column("Starting Price", width=150, anchor="center")
        item_treeview.heading("Buyer", text="Buyer")
        item_treeview.column("Buyer", width=100, anchor="center")
        item_treeview.heading("Ending Price", text="Ending Price")
        item_treeview.column("Ending Price", width=150, anchor="center")

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        edit_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        delete_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        item_treeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def update_items(self):
        pass