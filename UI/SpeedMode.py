import tkinter as tk
from tkinter import ttk, messagebox

from globals import ObjectType

class SpeedMode(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller

        self.item_var = tk.StringVar()
        self.buyer_var = tk.StringVar()
        self.ending_price_var = tk.StringVar()

        self.confirm_result = None

        speed_mode_label = ttk.Label(self, text="Speed Mode", font=("Arial", 16))
        instructions_label = ttk.Label(self, text="Press submit button or enter key to submit")

        item_label = ttk.Label(self, text="Item ID: ")
        buyer_label = ttk.Label(self, text="Buyer ID: ")
        ending_price_label = ttk.Label(self, text="Ending Price: ")

        self.item_entry = tk.Entry(self, textvariable=self.item_var)
        self.buyer_entry = tk.Entry(self, textvariable=self.buyer_var)
        self.ending_price_entry = tk.Entry(self, textvariable=self.ending_price_var)
        self.submit_button = ttk.Button(self, text="Submit Item", command=self.submit_changes)
        self.back_button = ttk.Button(self, text="Back to Items", command=lambda: parent.master.go_back())

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        speed_mode_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
        instructions_label.grid(row=1, column=0, columnspan=6, padx=10, pady=10)
        item_label.grid(row=2, column=0, padx=10, pady=10)
        self.item_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        buyer_label.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.buyer_entry.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        ending_price_label.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")
        self.ending_price_entry.grid(row=2, column=5, padx=10, pady=10, sticky="nsew")
        self.submit_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.back_button.grid(row=3, column=3, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.bind_all("<Return>", lambda event: self.submit_changes())

    def refresh(self):
        self.item_entry.delete(0, tk.END)
        self.buyer_entry.delete(0, tk.END)
        self.ending_price_entry.delete(0, tk.END)

    def submit_changes(self):
        def check_if_ids_are_present(item_id, buyer_id, ending_price):
            ret = True
            ret = ret & (item_id in self.controller.all_data.object_list[ObjectType.ITEM.value])
            ret = ret & (buyer_id in self.controller.all_data.object_list[ObjectType.BUYER.value])
            return ret

        item_id = self.item_var.get()
        buyer_id = self.buyer_var.get()
        ending_price = self.ending_price_var.get()
        if item_id == "" or buyer_id == "" or ending_price == "":
            messagebox.showwarning("Warning", "All fields must be non-empty") 
            return

        if check_if_ids_are_present(item_id, buyer_id, ending_price):
            if self.controller.all_data.object_list[ObjectType.ITEM.value][item_id].buyer == "":
                self.controller.all_data.edit_object(ObjectType.ITEM, id=item_id, buyer=buyer_id, ending_price=ending_price)
            else:
                confirm = PopupMessage(self, "This item already has data entered. Are you sure you want to edit the data? ", self.get_confirmation)
                if self.confirm_result:
                    self.controller.all_data.edit_object(ObjectType.ITEM, id=item_id, buyer=buyer_id, ending_price=ending_price)
                else:
                    pass
                    
            self.refresh()
        else:
            messagebox.showwarning("Warning", "Check that item and buyer IDs exist. ")

    def get_confirmation(self, result):
        self.confirm_result = result 

class PopupMessage(tk.Toplevel):
    def __init__(self, parent, message, callback):
        super().__init__(parent)
        self.callback = callback

        self.title("Confirm")
        message_label = ttk.Label(self, text=message)
        self.no_button = ttk.Button(self, text="No", command=self.no)
        self.yes_button = ttk.Button(self, text="Yes", command=self.yes)

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1)

        message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.no_button.grid(row=1, column=0, padx=10, pady=10)
        self.yes_button.grid(row=1, column=1, padx=10, pady=10)

        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)

    def no(self):
        self.callback(False)
        self.destroy()

    def yes(self):
        self.callback(True)
        self.destroy()
