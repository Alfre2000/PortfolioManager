from tkinter import *
from tkinter import ttk
from functions import graph, clear_frame


class EtfList(ttk.Frame):

    def __init__(self, root, portfolio):
        super().__init__(root)
        self.p = portfolio
        self.app = root.app
        self.names = tuple([x for x in self.p.etfs.keys()])
        self.etf_names = StringVar(value=self.names)
        self.lbox = Listbox(self, listvariable=self.etf_names, height=6)
        self.lbox.grid(row=0, column=0)
        self.lbox.bind('<<ListboxSelect>>', lambda e: self.etf_graph(self.names[self.lbox.curselection()[0]]))
        self.scroll = ttk.Scrollbar(self, orient=VERTICAL, command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1)
        for x in range(2):
            self.columnconfigure(x, weight=1)
        self.rowconfigure(0, weight=1)
    
    def etf_graph(self, etf):
        self.app.clear_radio()
        clear_frame(self.app.central_frame)
        fig, ax = self.p.get_etf_by_name(etf).equity_line()
        graph(fig, self.app.central_frame)
    
    def clear_box(self):
        self.lbox.select_clear(0,len(self.names)-1)