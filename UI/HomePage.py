import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create a label
        label = ttk.Label(self, text="Welcome to the Home Page!", font=("Arial", 16))
        # TODO: Implement donor page
        donorsButton = ttk.Button(self, text="Donors", command=lambda: controller.showFrame("DonorsPage"))
        # TODO: Implement item page
        itemsButton = ttk.Button(self, text="Items", command=lambda: controller.showFrame("ItemsPage"))
        # TODO: Implement bidder page
        biddersButton = ttk.Button(self, text="Bidders", command=lambda: controller.showFrame("BiddersPage"))
        # TODO: Implement receipt page
        receiptsButton = ttk.Button(self, text="Receipts", command=lambda: controller.showFrame("ReceiptsPage"))

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label           .grid(row=0, column=0, columnspan=2,                pady=10, sticky="nsew")
        donorsButton    .grid(row=1, column=0,                  padx=10,    pady=10, sticky="nsew")
        itemsButton     .grid(row=1, column=1,                  padx=10,    pady=10, sticky="nsew")
        biddersButton   .grid(row=2, column=0,                  padx=10,    pady=10, sticky="nsew")
        receiptsButton  .grid(row=2, column=1,                  padx=10,    pady=10, sticky="nsew")
