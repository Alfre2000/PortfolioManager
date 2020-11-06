from tkinter import *
from tkinter import filedialog
from pyetf.finance.portfolio import Portfolio
from tkinter import ttk


class MenuBar:

    def __init__(self, app):
        self.app = app
        self.main_page = self.app.main_page
        self.menu = Menu(app.root)
        self.fileMenu = Menu(self.menu)
        self.portfolioMenu = Menu(self.menu)
        self.menu.add_cascade(menu=self.fileMenu, label='File')
        self.fileMenu.add_command(label='Open...', command=self.openFile)
        self.menu.add_cascade(menu=self.portfolioMenu, label='Portafoglio')
        self.portfolioMenu.add_command(label='vs Indici', command=self.vs_indexes)
        app.root['menu'] = self.menu

    def openFile(self):
        """
        Change the Info file for the portfolio.
        :return None
        """
        filename = filedialog.askopenfilename()
        self.app.p = Portfolio(filename, self.app.server)
        self.main_page.left_frame.p = self.app.p
        self.main_page.right_frame.p = self.app.p
        self.main_page.right_frame.etf_list.p = self.app.p
        self.main_page.right_frame.etf_list.refresh()
        self.main_page.right_frame.add_etf.p = self.app.p
        self.main_page.right_frame.sell_etf.p = self.app.p
        self.main_page.left_frame.last_day()
    
    def vs_indexes(self):
        pass