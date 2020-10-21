from tkinter import *
from tkinter import ttk
from Frames.etf_list import EtfList
from Frames.add_etf import AddEtf
from Frames.sell_etf import SellEtf


class RightFrame(ttk.Frame):

    def __init__(self, root, app, portfolio):
        super().__init__(root)
        self.root = root
        self.app = app
        self.etf_list = EtfList(self, portfolio)
        self.etf_list.grid(row=0, column=0)
        AddEtf(self, portfolio).grid(row=1, column=0)
        SellEtf(self, portfolio).grid(row=2, column=0)
        for x in range(3):
            self.rowconfigure(x, weight=1)
        self.columnconfigure(0, weight=1)
