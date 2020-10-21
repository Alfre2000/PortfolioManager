from functions import configure
from tkinter import *
from tkinter import ttk
from Frames.etf_list import EtfList
from Frames.add_etf import AddEtf
from Frames.sell_etf import SellEtf


class RightFrame(ttk.Frame):
    """Class representing the right frame of the GUI"""

    def __init__(self, root, app, portfolio):
        """
        Initialize the class given a root Frame, the App Frame and the portfolio object.
        :param root: ttk.Frame 
        :param app: ttk.Frame
        :param portfolio: Portfolio
        :return None 
        """
        super().__init__(root)
        self.root = root
        self.app = app
        self.etf_list = EtfList(self, portfolio)
        self.etf_list.grid(row=0, column=0)
        AddEtf(self, portfolio).grid(row=1, column=0)
        SellEtf(self, portfolio).grid(row=2, column=0)
        configure(self, 3, 1)
