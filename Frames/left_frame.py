from tkinter import *
from tkinter import ttk
from functions import *


class LeftFrame(ttk.Frame):
    """Class representing the left frame of the GUI"""

    def __init__(self, root, app, portfolio):
        """
        Initialize the class given a root Frame, the App Frame and the portfolio object.
        :param root: ttk.Frame 
        :param app: ttk.Frame
        :param portfolio: Portfolio
        :return None 
        """
        super().__init__(root)
        self.app = app
        self.c_frame = self.app.central_frame
        self.p = portfolio
        ttk.Button(self, text='Dati Ultimo Giorno', command=self.last_day).grid(row=0, column=0)
        self.graph = StringVar()
        ttk.Radiobutton(self, text='Grafico Valore', command=self.draw_graph, variable=self.graph, value='value').grid(row=2, column=0)
        ttk.Radiobutton(self, text='Grafico Equity', command=self.draw_graph, variable=self.graph, value='equity').grid(row=3, column=0)
        ttk.Radiobutton(self, text='Grafico Investimento', command=self.draw_graph, variable=self.graph, value='invested').grid(row=4, column=0)
        ttk.Radiobutton(self, text='Grafico a Barre', command=self.draw_graph, variable=self.graph, value='bar').grid(row=5, column=0)
        ttk.Radiobutton(self, text='Grafico a Torta', command=self.draw_graph, variable=self.graph, value='pie').grid(row=6, column=0)
        ttk.Radiobutton(self, text='Tabella Investimenti', command=self.draw_table, variable=self.graph, value='inv_table').grid(row=8, column=0)
        ttk.Radiobutton(self, text='Tabella Portafoglio', command=self.draw_table, variable=self.graph, value='port_table').grid(row=9, column=0)
        ttk.Button(self, text='Statistiche', command=self.graph).grid(row=11, column=0)
        ttk.Button(self, text='Quit', command=root.quit).grid(row=13, column=0)
        configure(self, 14, 1)
    
    def draw_graph(self):
        """
        Draws a graph on the central frame given the radiobutton that has been selected.
        :return None
        """
        self.app.right_frame.etf_list.clear_box()
        clear_frame(self.c_frame)
        var = self.graph.get()
        if var == 'value':
            fig, ax = self.p.value_line()
        elif var == 'equity':
            fig, ax = self.p.equity_line()
        elif var == 'invested':
            fig, ax = self.p.investment_line()
        elif var == 'bar':
            fig, ax = self.p.bar_chart('M')
        else: # elif var == 'pie'
            fig, ax = self.p.pie_chart()
        graph(fig, self.c_frame)
    
    def last_day(self):
        """
        Shows data (P/L and P/L %) about the last trading day.
        :return None
        """
        clear_frame(self.c_frame)
        self.clear_radio()
        self.app.right_frame.etf_list.clear_box()
        table = self.p.last_day_table()
        ttk.Label(self.c_frame, text="DATI RELATIVI ALL'ULTIMA GIORNATA").grid(row=0, column=0, columnspan=3)
        ttk.Label(self.c_frame, text=self.p.data.index[-1].date().strftime('%A %d %B %Y')).grid(row=1, column=0, columnspan=3)
        ttk.Label(self.c_frame, text='Ticker').grid(row=2, column=0)
        ttk.Label(self.c_frame, text='Profit/Loss (€)').grid(row=2, column=1)
        ttk.Label(self.c_frame, text='Profit/Loss (%)').grid(row=2, column=2)
        for i, etf in enumerate(table.index):
            ttk.Label(self.c_frame, text=etf).grid(row=i+3, column=0)
            ttk.Label(self.c_frame, text=f'{round(table.loc[etf, "P/L"],2)} €').grid(row=i+3, column=1)
            ttk.Label(self.c_frame, text=f'{round(table.loc[etf, "P/L%"],2)} %').grid(row=i+3, column=2)
        configure(self.c_frame, len(table.index)+4, 3)
    
    def draw_table(self):
        """
        Shows data about investments or portfolio depending on the radiobutton cliccked.
        :return None
        """
        clear_frame(self.c_frame)
        self.app.right_frame.etf_list.clear_box()
        var = self.graph.get()
        if var == 'inv_table':
            table = self.p.investments_table()
            ttk.Label(self.c_frame, text="DATI RELATIVI AGLI INVESTIMENTI").grid(row=0, column=0, columnspan=len(table.columns))
            table.insert(1, 'Buying Date', table.index) 
        else:
            table = self.p.portfolio_table()
            ttk.Label(self.c_frame, text="DATI RELATIVI AL PORTAFOGLIO").grid(row=0, column=0, columnspan=len(table.columns))
            table.insert(0, 'Ticker', table.index) 
        table['Idx'] = [x for x in range(len(table))]
        table.set_index('Idx', inplace=True)  
        for i, col in enumerate(table.columns):
            ttk.Label(self.c_frame, text=col).grid(row=1, column=i)
        for y in table.index:
            for x, col in enumerate(table.columns):
                ttk.Label(self.c_frame, text=table.loc[y, col]).grid(row=y+2, column=x)
        configure(self.c_frame, len(table.index)+2, len(table.columns))
    
    def clear_radio(self):
        """
        Deselect every radiobutton. 
        :return None
        """
        for children in self.winfo_children():
            if isinstance(children, ttk.Radiobutton):
                children.state(['!selected'])