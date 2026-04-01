import tkinter as tk
from tkinter import ttk

class DonorsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        treeview_columns = ("ID", "Name", "Address", "Items")

        # Create a label
        label = ttk.Label(self, text="Donors", font=("Arial", 16))
        # TODO: Add add donor page
        add_button = ttk.Button(self, text="Add Donor", command=lambda: parent.master.show_frame("UnfinishedPage"))
        # TODO: Add edit donor page
        edit_button = ttk.Button(self, text="Edit Donor", command=lambda: parent.master.show_frame("UnfinishedPage"))
        # TODO: Add delete donor page
        delete_button = ttk.Button(self, text="Delete Donor", command=lambda: parent.master.show_frame("UnfinishedPage"))
        back_button = ttk.Button(self, text="Back to Home", command=lambda: parent.master.go_back())
        donor_treeview = ttk.Treeview(self, columns=treeview_columns, show="headings")

        donor_treeview.heading("ID", text="ID")
        donor_treeview.column("ID", width=50, anchor="center")
        donor_treeview.heading("Name", text="Name")
        donor_treeview.column("Name", width=100, anchor="center")
        donor_treeview.heading("Address", text="Address")
        donor_treeview.column("Address", width=150, anchor="center")
        donor_treeview.heading("Items", text="Items Donated")
        donor_treeview.column("Items", width=100, anchor="center")

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
        donor_treeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def update_donors(self):
        pass