import tkinter as tk
from tkinter import ttk

class UnfinishedPage(tk.Frame):
    def __init__(self, parent, controller, nav):
        super().__init__(parent)
        self.controller = controller
        self.nav = nav

        # Create a label
        label = ttk.Label(self, text="This page is under construction.", font=("Arial", 16))
        backButton = ttk.Button(self, text="Back to Home", command=lambda: parent.master.goBack())

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label.grid(row=0, column=0, padx=10, pady=10)
        backButton.grid(row=1, column=0, padx=10, pady=10)