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

class ModPersonForm(tk.Frame):
    def __init__(self, parent, controller, person_type, person_type_label, callback=None):
        super().__init__(parent)
        self.controller = controller
        self.type = person_type
        self.person_type_label = person_type_label
        self.callback = callback

        self.name_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.next_id = tk.StringVar()
        ID_label = ttk.Label(self, text="ID")
        name_label = ttk.Label(self, text="Name")
        address_label = ttk.Label(self, text="Address")
        ID_entry = tk.Entry(self, textvariable=self.next_id, state="readonly")
        self.name_entry = ttk.Entry(self, textvariable=self.name_var)
        self.address_entry = ttk.Entry(self, textvariable=self.address_var)

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)
        self.grid_columnconfigure(2)
        self.grid_columnconfigure(3)

        ID_label.grid(row=1, column=0, padx=10, pady=10)
        ID_entry.grid(row=1, column=1, padx=10, pady=10)
        name_label.grid(row=1, column=2, padx=10, pady=10)
        self.name_entry.grid(row=1, column=3, padx=10, pady=10)
        address_label.grid(row=2, column=0, padx=10, pady=10)
        self.address_entry.grid(row=2, column=1, columnspan=3, sticky="ew", padx=10, pady=10)

        self.next_id.set(self.controller.all_data.next_ids[self.type.value])

        add_or_edit = AddOrEdit(self, controller, self.type, self.person_type_label, callback=self.on_mode_change)
        add_or_edit.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

    def on_mode_change(self, modeIn):
        self.mode = modeIn
        if modeIn == "ADD":
            self.next_id.set(self.controller.all_data.next_ids[self.type.value])
            self.name_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.submit_button = ttk.Button(self, text=f"Add {self.person_type_label}", command=self.commit_action)
            self.submit_button.grid(row=3, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
        elif modeIn == "EDIT":
            self.next_id.set("")
            self.submit_button = ttk.Button(self, text=f"Edit {self.person_type_label}", command=self.commit_action)
            self.submit_button.grid(row=3, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

    def commit_action(self):
        if self.mode == "ADD":
            if self.name_var.get() == "" or self.address_var.get() == "":
                return
            self.controller.all_data.create_object(self.type, idIn=self.next_id.get(), nameIn=self.name_var.get(), addressIn=self.address_var.get())
            self.next_id.set(self.controller.all_data.next_ids[self.type.value])
            self.name_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        elif self.mode == "EDIT":
            if self.next_id.get() == "": # Occurs when shifting from Add to Edit mode
                return
            if self.name_var.get() == "" or self.address_var.get() == "":
                return
            person = self.controller.all_data.object_list[self.type.value][self.next_id.get()]
            person.name = self.name_var.get()
            person.address = self.address_var.get()
            person.save()
        else:
            pass

        self.callback()

    def set_fields_on_parent_request(self, idIn, nameIn, addressIn):
        if self.mode == "EDIT":
            if idIn is not None:
                self.next_id.set(idIn)
                self.name_var.set(nameIn) 
                self.address_var.set(addressIn) 
            else:
                self.next_id.set("")
                self.name_entry.delete(0, tk.END)
                self.address_entry.delete(0, tk.END)

class PersonsPage(tk.Frame):
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

        treeview_columns = ("ID", "Name", "Address", "Items")

        self.person_type_label = self.type.name.capitalize()

        label = ttk.Label(self, text=f"{self.person_type_label}s", font=("Arial", 16))
        label_frame = ttk.LabelFrame(self, text="Add/Edit", relief="ridge", borderwidth=3)
        self.mod_frame = ModPersonForm(label_frame, controller, self.type, self.person_type_label, callback=self.update_persons)
        self.mod_frame.pack()

        delete_button = ttk.Button(self, text=f"Delete {self.person_type_label}", command=self.delete_person)
        back_button = ttk.Button(self, text="Back to Home", command=lambda: parent.master.go_back())
        self.person_treeview = ttk.Treeview(self, columns=treeview_columns, show="headings")
        self.person_treeview.bind("<<TreeviewSelect>>", self.on_tree_click)

        self.person_treeview.heading("ID", text="ID")
        self.person_treeview.column("ID", width=50, anchor="center")
        self.person_treeview.heading("Name", text="Name")
        self.person_treeview.column("Name", width=100, anchor="center")
        self.person_treeview.heading("Address", text="Address")
        self.person_treeview.column("Address", width=150, anchor="center")
        self.person_treeview.heading("Items", text=f"Items {determine_donated_or_bought(self.type)}")
        self.person_treeview.column("Items", width=100, anchor="center")

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
        self.person_treeview.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")

    # TODO: Write function to update the treeview
    def update_persons(self):
        for row in self.person_treeview.get_children():
            self.person_treeview.delete(row)
        for person in self.controller.all_data.object_list[self.type.value]:
            person_object = self.controller.all_data.object_list[self.type.value][person]
            self.person_treeview.insert("", tk.END, values=(person_object.id, person_object.name, person_object.address))

    def delete_person(self):
        selection = self.person_treeview.selection()
        if not selection:
            return
        
        person_id = self.person_treeview.item(selection[0], "values")[0]
        self.controller.all_data.delete_object(self.type, person_id)
        self.mod_frame.set_fields_on_parent_request(None, None, None)
        self.update_persons()

    def on_tree_click(self, event):
        selection = self.person_treeview.selection()
        if not selection:
            return
        
        values = self.person_treeview.item(selection[0], "values")
        self.mod_frame.set_fields_on_parent_request(values[0], values[1], values[2])