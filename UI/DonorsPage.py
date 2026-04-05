import tkinter as tk
from tkinter import ttk

class AddOrEdit(tk.Frame):
    def __init__(self, parent, controller, callback=None):
        super().__init__(parent)
        self.controller = controller
        self.callback = callback
        self.mode = tk.StringVar()
        mode_add = tk.Radiobutton(self, text="Add donor", variable=self.mode, value="ADD", command=self._notify_parents)
        mode_edit = tk.Radiobutton(self, text="Edit donor", variable=self.mode, value="EDIT", command=self._notify_parents)

        self.grid_rowconfigure(0)    
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)

        mode_add.grid(row=0, column=0, padx=10, pady=10)
        mode_edit.grid(row=0, column=1, padx=10, pady=10)

    def _notify_parents(self):
        if self.callback:
            self.callback(self.mode.get())

class ModDonorForm(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.next_id = tk.StringVar()
        add_or_edit = AddOrEdit(self, controller, callback=self.on_mode_change)
        ID_label = ttk.Label(self, text="ID")
        name_label = ttk.Label(self, text="Name")
        address_label = ttk.Label(self, text="Address")
        ID_entry = tk.Entry(self, textvariable=self.next_id, state="readonly")
        name_entry = ttk.Entry(self)
        address_entry = ttk.Entry(self)
        self.submit_button = ttk.Button(self, text="Submit")

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)
        self.grid_columnconfigure(2)
        self.grid_columnconfigure(3)

        add_or_edit.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        ID_label.grid(row=1, column=0, padx=10, pady=10)
        ID_entry.grid(row=1, column=1, padx=10, pady=10)
        name_label.grid(row=1, column=2, padx=10, pady=10)
        name_entry.grid(row=1, column=3, padx=10, pady=10)
        address_label.grid(row=2, column=0, padx=10, pady=10)
        address_entry.grid(row=2, column=1, columnspan=3, sticky="ew", padx=10, pady=10)
        self.submit_button.grid(row=3, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        self.next_id.set(self.controller.all_data.next_donor_id)

    def on_mode_change(self, modeIn):
        if modeIn == "ADD":
            self.next_id.set(self.controller.all_data.next_donor_id)
            # TODO: Change submit button based on the mode
            # self.submit_button
        elif modeIn == "EDIT":
            self.next_id.set("Unfinished")

class DonorsPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        treeview_columns = ("ID", "Name", "Address", "Items")

        # Create a label
        label = ttk.Label(self, text="Donors", font=("Arial", 16))
        # TODO: Add add donor page
        label_frame = ttk.LabelFrame(self, text="Add/Edit", relief="ridge", borderwidth=3)
        mod_frame = ModDonorForm(label_frame, controller).pack()
        # TODO: Add edit donor page
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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        donor_treeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def update_donors(self):
        pass