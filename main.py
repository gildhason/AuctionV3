import tkinter as tk
from tkinter import ttk
from UI.Auction import Auction
from Logic.AllData import AllData

if __name__ == "__main__":
    all_data = AllData()
    Auction(all_data).mainloop()
