import tkinter as tk
from tkinter import ttk

from globals import ObjectType
from Logic.Classes import Donor
from Logic.Classes import Buyer

class AddOrEdit(tk.Frame):
    def __init__(self, parent, controller, person_type, person_type_label, callback=None):
        super().__init__(parent)
        self.controller = controller
        self.type = person_type
        self.person_type_label = person_type_label
        self.callback = callback
        self.mode = tk.StringVar()
        mode_add = tk.Radiobutton(self, text=f"Add {self.person_type_label}", variable=self.mode, value="ADD", command=self._notify_parents)
        mode_edit = tk.Radiobutton(self, text=f"Edit {self.person_type_label}", variable=self.mode, value="EDIT", command=self._notify_parents)

        self.mode.set("ADD")

        self.grid_rowconfigure(0)    
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)

        mode_add.grid(row=0, column=0, padx=10, pady=10)
        mode_edit.grid(row=0, column=1, padx=10, pady=10)

        self._notify_parents()

    def _notify_parents(self):
        if self.callback:
            self.callback(self.mode.get())

class ModObjectForm(tk.Frame):
    donor_list = []
    buyer_list = []

    def __init__(self, parent, controller, person_type, person_type_label, callback=None):
        super().__init__(parent)
        self.controller = controller
        self.type = person_type
        self.person_type_label = person_type_label
        self.callback = callback
        self.treeview_params = {
            "id": "",
            "name": "",
            "address": "",
            "donor": "",
            "starting_price": "",
            "buyer": "",
            "ending_price": "",
        }

        self.name_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.donor_var = tk.StringVar()
        self.starting_price_var = tk.StringVar()
        self.buyer_var = tk.StringVar()
        self.ending_price_var = tk.StringVar()

        self.mode = None

        self.next_id = tk.StringVar()
        ID_label = ttk.Label(self, text="ID")
        name_label = ttk.Label(self, text="Name")
        address_label = ttk.Label(self, text="Address")
        donor_label = ttk.Label(self, text="Donor")
        starting_price_label = ttk.Label(self, text="Starting Price")
        buyer_label = ttk.Label(self, text="Buyer")
        ending_price_label = ttk.Label(self, text="Ending Price")
        ID_entry = tk.Entry(self, textvariable=self.next_id, state="normal" if self.type == ObjectType.BUYER else "readonly")
        self.name_entry = ttk.Entry(self, textvariable=self.name_var)
        self.address_entry = ttk.Entry(self, textvariable=self.address_var)
        self.donor_combo = ttk.Combobox(self, textvariable=self.donor_var, values=ModObjectForm.donor_list)
        self.starting_price_entry = ttk.Entry(self, textvariable=self.starting_price_var)
        self.buyer_combo = ttk.Combobox(self, textvariable=self.buyer_var, values=ModObjectForm.buyer_list)
        self.ending_price_entry = ttk.Entry(self, textvariable=self.ending_price_var)

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)
        self.grid_columnconfigure(2)
        self.grid_columnconfigure(3)
        if self.type == ObjectType.ITEM:
            self.grid_rowconfigure(4)

        ID_label.grid(row=1, column=0, padx=10, pady=10)
        ID_entry.grid(row=1, column=1, padx=10, pady=10)
        name_label.grid(row=1, column=2, padx=10, pady=10)
        self.name_entry.grid(row=1, column=3, padx=10, pady=10)
        if self.type != ObjectType.ITEM:
            address_label.grid(row=2, column=0, padx=10, pady=10)
            self.address_entry.grid(row=2, column=1, columnspan=3, sticky="ew", padx=10, pady=10)
        else:
            donor_label.grid(row=2, column=0, padx=10, pady=10)
            self.donor_combo.grid(row=2, column=1, padx=10, pady=10)
            starting_price_label.grid(row=2, column=2, padx=10, pady=10)
            self.starting_price_entry.grid(row=2, column=3, padx=10, pady=10)
            buyer_label.grid(row=3, column=0, padx=10, pady=10)
            self.buyer_combo.grid(row=3, column=1, padx=10, pady=10)
            ending_price_label.grid(row=3, column=2, padx=10, pady=10)
            self.ending_price_entry.grid(row=3, column=3, padx=10, pady=10)

        self.next_id.set(self.controller.all_data.next_ids[self.type.value])

        add_or_edit = AddOrEdit(self, controller, self.type, self.person_type_label, callback=self.on_mode_change)
        add_or_edit.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

    def on_mode_change(self, modeIn):
        if self.mode == modeIn:
            return
        self.mode = modeIn
        submit_button_row = 3 if self.type != ObjectType.ITEM else 4
        if modeIn == "ADD":
            self.next_id.set(self.controller.all_data.next_ids[self.type.value])
            self.name_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.donor_combo.delete(0, tk.END)
            self.starting_price_entry.delete(0, tk.END)
            self.buyer_combo.delete(0, tk.END)
            self.ending_price_entry.delete(0, tk.END)
            self.submit_button = ttk.Button(self, text=f"Add {self.person_type_label}", command=self.commit_action)
        elif modeIn == "EDIT":
            self.set_fields_on_request()
            self.submit_button = ttk.Button(self, text=f"Edit {self.person_type_label}", command=self.commit_action)
        self.submit_button.grid(row=submit_button_row, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

    def commit_action(self):
        if self.mode == "ADD":
            if self.next_id.get() == "":
                return
            if self.type != ObjectType.ITEM:
                if self.name_var.get() == "" or self.address_var.get() == "":
                    return
                if self.type == ObjectType.BUYER and self.next_id.get() in self.controller.all_data.object_list[ObjectType.BUYER.value].keys():
                    return
            else:
                if self.name_var.get() == "":
                    return

            self.controller.all_data.create_object(self.type, id=self.next_id.get(), name=self.name_var.get(), address=self.address_var.get(), donor=self.donor_var.get().split(":")[0], starting_price=self.starting_price_var.get(), buyer=self.buyer_var.get().split(":")[0], ending_price=self.ending_price_var.get())
            self.next_id.set(self.controller.all_data.next_ids[self.type.value])
            self.name_entry.delete(0, tk.END)
            if self.type != ObjectType.ITEM:
                self.address_entry.delete(0, tk.END)
            else:
                self.donor_combo.delete(0, tk.END)
                self.starting_price_entry.delete(0, tk.END)
                self.buyer_combo.delete(0, tk.END)
                self.ending_price_entry.delete(0, tk.END)
        elif self.mode == "EDIT":
            if self.next_id.get() == "": # Occurs when shifting from Add to Edit mode
                return
            if self.type != ObjectType.ITEM:
                if self.name_var.get() == "" or self.address_var.get() == "":
                    return
            else:
                if self.name_var.get() == "":
                    return
            self.controller.all_data.edit_object(self.type, id=self.next_id.get(), name=self.name_var.get(), address=self.address_var.get(), donor=self.donor_var.get().split(":")[0], starting_price=self.starting_price_var.get(), buyer=self.buyer_var.get().split(":")[0], ending_price=self.ending_price_var.get())
        else:
            pass

        self.callback()

    def set_fields_on_request(self):
        if self.mode == "EDIT":
            if self.treeview_params["id"] != "":
                self.next_id.set(self.treeview_params["id"])
                self.name_var.set(self.treeview_params["name"]) 
                self.address_var.set(self.treeview_params["address"]) 
                self.donor_var.set(self.treeview_params["donor"])
                self.starting_price_var.set(self.treeview_params["starting_price"])
                self.buyer_var.set(self.treeview_params["buyer"])
                self.ending_price_var.set(self.treeview_params["ending_price"])
            else:
                self.next_id.set("")
                self.name_entry.delete(0, tk.END)
                self.address_entry.delete(0, tk.END)

class ObjectsPage(tk.Frame):
    def __init__(self, parent, controller, person_type, nav):
        def determine_donated_or_bought(person_type):
            if person_type == ObjectType.DONOR:
                return "Donated"
            elif person_type == ObjectType.BUYER:
                return "Bought"
            else:
                return "ERROR"

        super().__init__(parent)
        self.controller = controller
        self.type = person_type
        self.nav = nav

        treeview_columns = None
        if self.type == ObjectType.DONOR:
            treeview_columns = ("ID", "Name", "Address", "Items")
        elif self.type == ObjectType.ITEM:
            treeview_columns = ("ID", "Name", "Donor", "Starting Price", "Buyer", "Ending Price")
        elif self.type == ObjectType.BUYER:
            treeview_columns = ("ID", "Name", "Address", "Items", "Amount Owed")

        self.person_type_label = self.type.name.capitalize()

        label = ttk.Label(self, text=f"{self.person_type_label}s", font=("Arial", 16))
        label_frame = ttk.LabelFrame(self, text="Add/Edit", relief="ridge", borderwidth=3)
        self.mod_frame = ModObjectForm(label_frame, controller, self.type, self.person_type_label, callback=self.update_objects)
        self.mod_frame.pack()

        delete_button = ttk.Button(self, text=f"Delete {self.person_type_label}", command=self.delete_object)
        duplicate_button = ttk.Button(self, text=f"Duplicate {self.person_type_label}", command=self.delete_object)
        speed_mode_button = ttk.Button(self, text=f"Enter Speed Mode", command=self.delete_object)
        back_button = ttk.Button(self, text="Back to Home", command=lambda: parent.master.go_back())
        self.object_treeview = ttk.Treeview(self, columns=treeview_columns, show="headings")
        self.object_treeview.bind("<<TreeviewSelect>>", self.on_tree_click)

        if self.type == ObjectType.DONOR:
            self.object_treeview.heading("ID", text="ID")
            self.object_treeview.column("ID", width=50, anchor="center")
            self.object_treeview.heading("Name", text="Name")
            self.object_treeview.column("Name", width=100, anchor="center")
            self.object_treeview.heading("Address", text="Address")
            self.object_treeview.column("Address", width=150, anchor="center")
            self.object_treeview.heading("Items", text=f"Items {determine_donated_or_bought(self.type)}")
            self.object_treeview.column("Items", width=100, anchor="center")
        if self.type == ObjectType.ITEM:
            self.object_treeview.heading("ID", text="ID")
            self.object_treeview.column("ID", width=50, anchor="center")
            self.object_treeview.heading("Name", text="Name")
            self.object_treeview.column("Name", width=100, anchor="center")
            self.object_treeview.heading("Donor", text="Donor")
            self.object_treeview.column("Donor", width=150, anchor="center")
            self.object_treeview.heading("Starting Price", text=f"Starting Price")
            self.object_treeview.column("Starting Price", width=100, anchor="center")
            self.object_treeview.heading("Buyer", text="Buyer")
            self.object_treeview.column("Buyer", width=150, anchor="center")
            self.object_treeview.heading("Ending Price", text=f"Ending Price")
            self.object_treeview.column("Ending Price", width=100, anchor="center")
        if self.type == ObjectType.BUYER:
            self.object_treeview.heading("ID", text="ID")
            self.object_treeview.column("ID", width=50, anchor="center")
            self.object_treeview.heading("Name", text="Name")
            self.object_treeview.column("Name", width=100, anchor="center")
            self.object_treeview.heading("Address", text="Address")
            self.object_treeview.column("Address", width=150, anchor="center")
            self.object_treeview.heading("Items", text=f"Items {determine_donated_or_bought(self.type)}")
            self.object_treeview.column("Items", width=100, anchor="center")
            self.object_treeview.heading("Amount Owed", text=f"Amount Owed")
            self.object_treeview.column("Amount Owed", width=100, anchor="center")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        spacer = tk.Label(self, text="")
        if self.type == ObjectType.ITEM:
            duplicate_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
            speed_mode_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
            back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
            self.object_treeview.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")
        else:
            spacer.grid(row=3, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
            back_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
            self.object_treeview.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

    def refresh(self):
        self.update_objects()

    def update_objects(self):
        for row in self.object_treeview.get_children():
            self.object_treeview.delete(row)
        for object in self.controller.all_data.object_list[self.type.value]:
            this_object = self.controller.all_data.object_list[self.type.value][object]
            if self.type == ObjectType.DONOR:
                self.object_treeview.insert("", tk.END, values=(this_object.id, this_object.name, this_object.address, ", ".join(this_object.items)))
            elif self.type == ObjectType.ITEM:
                donor_str = "" if this_object.donor == "" else f"{this_object.donor}: {self.controller.all_data.object_list[ObjectType.DONOR.value][this_object.donor].name}"
                buyer_str = "" if this_object.buyer == "" else f"{this_object.buyer}: {self.controller.all_data.object_list[ObjectType.BUYER.value][this_object.buyer].name}"
                self.object_treeview.insert("", tk.END, values=(this_object.id, this_object.name, donor_str, this_object.starting_price, buyer_str, this_object.ending_price))
            if self.type == ObjectType.BUYER:
                self.object_treeview.insert("", tk.END, values=(this_object.id, this_object.name, this_object.address, ", ".join(this_object.items), self.controller.all_data.get_amount_owed(this_object)))

        self.controller.frames["ItemsPage"].mod_frame.donor_combo["values"] = [f"{id}: {donor.name}" for id, donor in self.controller.all_data.object_list[ObjectType.DONOR.value].items()]
        self.controller.frames["ItemsPage"].mod_frame.buyer_combo["values"] = [f"{id}: {buyer.name}" for id, buyer in self.controller.all_data.object_list[ObjectType.BUYER.value].items()]

    def delete_object(self):
        selection = self.object_treeview.selection()
        if not selection:
            return
        
        object_id = self.object_treeview.item(selection[0], "values")[0]
        self.controller.all_data.delete_object(self.type, object_id)
        values_dict = {
            "id": "",
            "name": "",
            "address": "",
            "donor": "",
            "starting_price": "",
            "buyer": "",
            "ending_price": "",
        }
        self.mod_frame.treeview_params = values_dict
        self.mod_frame.set_fields_on_request()
        if self.type == ObjectType.BUYER:
            self.mod_frame.next_id.set(self.controller.all_data.next_ids[self.type.value])
        self.update_objects()

    def on_tree_click(self, event):
        selection = self.object_treeview.selection()
        if not selection:
            return
        
        values = self.object_treeview.item(selection[0], "values")
        values_dict = {
            "id": values[0],
            "name": values[1]
        }
        if self.type != ObjectType.ITEM:
            values_dict.update({
                "address": values[2],
                "donor": "",
                "starting_price": "",
                "buyer": "",
                "ending_price": "",
            })
            self.mod_frame.treeview_params = values_dict
            self.mod_frame.set_fields_on_request()
        else:
            values_dict.update({
                "address": "",
                "donor": values[2],
                "starting_price": values[3],
                "buyer": values[4],
                "ending_price": values[5]
            })
            self.mod_frame.treeview_params = values_dict
            self.mod_frame.set_fields_on_request()
