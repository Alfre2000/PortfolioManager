from tkinter import *
from tkinter import ttk
from matplotlib.pyplot import text
from portfolio import Portfolio
from etf import ETF
from datetime import date
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class AddEtf(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        ttk.Label(self, text='AGGIUNGI ETF').grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text='Ticker', anchor='w', justify='left').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self, text='Data Acquisto', anchor='w', justify='left').grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self, text='Numero di Azioni', anchor='w', justify='left').grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(self, text="Prezzo d'Acquisto", anchor='w', justify='left').grid(row=4, column=0, padx=5, pady=5)
        ttk.Label(self, text='Commissioni', anchor='w', justify='left').grid(row=5, column=0, padx=5, pady=5)
        self.tickerVar = StringVar()
        self.dateVar = StringVar(value='Es. 10-12-2020')
        self.nVar = IntVar()
        self.priceVar = DoubleVar()
        self.commVar = DoubleVar()
        ttk.Entry(self, textvariable=self.tickerVar, width=12).grid(row=1, column=1)    
        self.e = ttk.Entry(self, textvariable=self.dateVar, width=12)
        self.e.grid(row=2, column=1)   
        ttk.Entry(self, textvariable=self.nVar, width=12).grid(row=3, column=1)           
        ttk.Entry(self, textvariable=self.priceVar, width=12).grid(row=4, column=1)           
        ttk.Entry(self, textvariable=self.commVar, width=12).grid(row=5, column=1) 
        self.result = ttk.Label(self, text='')
        self.result.grid(row=6, column=1) 
        self.button = ttk.Button(self, text='Aggiungi', command=self.add_etf)
        self.button.grid(row=6, column=0, pady=10)

    def add_etf(self):
        day = self.e.get().split('-')
        try:
            p.add_etf(ETF(self.tickerVar.get(), date(int(day[2]), int(day[1]), int(day[0])), self.nVar.get(), self.priceVar.get(), self.commVar.get()))     
            self.tickerVar.set('')
            self.dateVar.set('')
            self.priceVar.set('')
            self.commVar.set('')
            self.result.configure(text='ETF aggiunyo !')
        except:
            self.result.configure(text='Errore !')       

class SellEtf(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        ttk.Label(self, text='VENDI ETF').grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text='Ticker', anchor='w', justify='left').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self, text='Data Vendita', anchor='w', justify='left').grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self, text="Prezzo di Vendita", anchor='w', justify='left').grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(self, text='Commissioni', anchor='w', justify='left').grid(row=4, column=0, padx=5, pady=5)
        self.tickerVar = StringVar()
        self.dateVar = StringVar(value='Es. 10-12-2020')
        self.priceVar = DoubleVar()
        self.commVar = DoubleVar()
        ttk.Entry(self, textvariable=self.tickerVar, width=12).grid(row=1, column=1)    
        self.e = ttk.Entry(self, textvariable=self.dateVar, width=12)
        self.e.grid(row=2, column=1)   
        ttk.Entry(self, textvariable=self.priceVar, width=12).grid(row=3, column=1)           
        ttk.Entry(self, textvariable=self.commVar, width=12).grid(row=4, column=1) 
        self.result = ttk.Label(self, text='')
        self.result.grid(row=5, column=1) 
        self.button = ttk.Button(self, text='Vendi', command=self.sell_etf)
        self.button.grid(row=5, column=0, pady=10)

    def sell_etf(self):
        day = self.e.get().split('-')
        try:
            p.sell_etf(self.tickerVar.get(), date(int(day[2]), int(day[1]), int(day[0])), self.priceVar.get(), self.commVar.get())       
            self.tickerVar.set('')
            self.dateVar.set('')
            self.priceVar.set('')
            self.commVar.set('')
            self.result.configure(text='ETF sold !')
        except:
            self.result.configure(text='Errore !')

class App:

    def __init__(self, root):
        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for y in range(7):
            self.mainframe.columnconfigure(y, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        # ------------------------------------LEFT FRAME---------------------------------------------------- #
        self.left_frame = ttk.Frame(self.mainframe)
        self.left_frame.grid(row=0, column=0, sticky=(W, N, S, E), padx=15)
        # ------------------------------------LEFT WIDGETS-------------------------------------------------- #
        self.recap_button = ttk.Button(self.left_frame, text='Dati Ultimo Giorno', command=self.last_day)
        self.recap_button.grid(row=0, column=0)
        self.graph = StringVar()
        self.valueGraph = ttk.Radiobutton(self.left_frame, text='Grafico Valore', command=self.value_line, variable=self.graph, value='value')
        self.valueGraph.grid(row=2, column=0)
        self.equityGraph = ttk.Radiobutton(self.left_frame, text='Grafico Equity', command=self.equity_line, variable=self.graph, value='equity')
        self.equityGraph.grid(row=3, column=0)
        self.investedGraph = ttk.Radiobutton(self.left_frame, text='Grafico Investimento', command=self.invested_line, variable=self.graph, value='invested')
        self.investedGraph.grid(row=4, column=0)
        self.barGraph = ttk.Radiobutton(self.left_frame, text='Grafico a Barre', command=self.bar_chart, variable=self.graph, value='bar')
        self.barGraph.grid(row=5, column=0)
        self.pieGraph = ttk.Radiobutton(self.left_frame, text='Grafico a Torta', command=self.pie_chart, variable=self.graph, value='pie')
        self.pieGraph.grid(row=6, column=0)
        self.investmentTable = ttk.Radiobutton(self.left_frame, text='Tabella Investimenti', command=self.investment_table, variable=self.graph, value='inv_table')
        self.investmentTable.grid(row=8, column=0)
        self.portfolioTable = ttk.Radiobutton(self.left_frame, text='Tabella Portafoglio', command=self.portfolio_table, variable=self.graph, value='port_table')
        self.portfolioTable.grid(row=9, column=0)
        self.stats_button = ttk.Button(self.left_frame, text='Statistiche', command=self.stats)
        self.stats_button.grid(row=11, column=0)
        self.quit_button = ttk.Button(self.left_frame, text='Quit', command=root.quit)
        self.quit_button.grid(row=13, column=0)
        for x in range(14):
            self.left_frame.rowconfigure(x, weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        # --------------------------------------CENTER FRAME------------------------------------------------- #
        self.central_frame = ttk.Frame(self.mainframe)
        self.central_frame.grid(row=0, column=1, columnspan=5, sticky=(E, W, N, S), padx=15)
        # --------------------------------------RIGHT FRAME-------------------------------------------------- #
        self.right_frame = ttk.Frame(self.mainframe)
        self.right_frame.grid(row=0, column=6, sticky=(E, N, S, W), padx=15)
        # --------------------------------------RIGHT WIDGES------------------------------------------------- #
        self.list_frame = ttk.Frame(self.right_frame)
        self.list_frame.grid(row=0, column=0)
        self.etf_names = tuple([x for x in p.etfs.keys()])
        self.names = StringVar(value=self.etf_names)
        self.lbox = Listbox(self.list_frame, listvariable=self.names, height=6)
        self.lbox.grid(row=0, column=0)
        self.lbox.bind('<<ListboxSelect>>', lambda e: self.etf_graph(self.lbox.curselection()))
        self.scroll = ttk.Scrollbar(self.list_frame, orient=VERTICAL, command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1)
        for y in range(2):
            self.list_frame.columnconfigure(y, weight=1)
        self.list_frame.rowconfigure(0, weight=1)
        self.add_frame = AddEtf(self.right_frame)
        self.add_frame.grid(row=1, column=0)
        self.sell_frame = SellEtf(self.right_frame)
        self.sell_frame.grid(row=2, column=0)
        for x in range(3):
            self.right_frame.rowconfigure(x, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        
        self.last_day()

    def last_day(self):
        self.clear_frame(self.central_frame)
        self.clear_radio()
        self.clear_list_box()
        table = p.last_day_table()
        ttk.Label(self.central_frame, text="DATI RELATIVI ALL'ULTIMA GIORNATA").grid(row=0, column=0, columnspan=3)
        ttk.Label(self.central_frame, text=p.data.index[-1].date().strftime('%A %d %B %Y')).grid(row=1, column=0, columnspan=3)
        ttk.Label(self.central_frame, text='Ticker').grid(row=2, column=0)
        ttk.Label(self.central_frame, text='Profit/Loss (€)').grid(row=2, column=1)
        ttk.Label(self.central_frame, text='Profit/Loss (%)').grid(row=2, column=2)
        count = 3
        for etf in table.index:
            ttk.Label(self.central_frame, text=etf).grid(row=count, column=0)
            ttk.Label(self.central_frame, text=f'{round(table.loc[etf, "P/L"],2)} €').grid(row=count, column=1)
            ttk.Label(self.central_frame, text=f'{round(table.loc[etf, "P/L%"],2)} %').grid(row=count, column=2)
            count += 1
        for y in range(3):
            self.central_frame.columnconfigure(y, weight=1)
        for x in range(len(table.index)+3+1):
            self.central_frame.rowconfigure(x, weight=1)
    
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    def clear_radio(self):
        self.equityGraph.state(['!selected'])
        self.valueGraph.state(['!selected'])
        self.investedGraph.state(['!selected'])
        self.barGraph.state(['!selected'])
        self.pieGraph.state(['!selected'])
        self.investmentTable.state(['!selected'])
        self.portfolioTable.state(['!selected'])
    
    def clear_list_box(self):
        self.lbox.select_clear(0,len(self.etf_names)-1)
    
    def value_line(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        fig, ax = p.value_line()
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)

    
    def equity_line(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        fig, ax = p.equity_line()
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)

    def invested_line(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        fig, ax = p.investment_line()
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)
    
    def bar_chart(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        fig, ax = p.bar_chart("M")
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)
    
    def pie_chart(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        fig, ax = p.pie_chart()
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)
    
    def investment_table(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        table = p.investments_table()
        table.insert(0, 'Buying Date', table.index)
        table['Idx'] = [x for x in range(len(table))]
        table.set_index('Idx', inplace=True)  
        ttk.Label(self.central_frame, text="DATI RELATIVI AGLI INVESTIMENTI").grid(row=0, column=0, columnspan=len(table.columns))
        for i, col in enumerate(table.columns):
            ttk.Label(self.central_frame, text=col).grid(row=1, column=i)
        for y in table.index:
            for x, col in enumerate(table.columns):
                ttk.Label(self.central_frame, text=table.loc[y, col]).grid(row=y+2, column=x)
        for x in range(len(table.index)+2):
            self.central_frame.rowconfigure(x, weight=1)
        for y in range(len(table.columns)):
            self.central_frame.columnconfigure(y, weight=1)

    def portfolio_table(self):
        self.clear_frame(self.central_frame)
        self.clear_list_box()
        table = p.porfolio_table()
        ttk.Label(self.central_frame, text="DATI RELATIVI AL PORTAFOGLIO").grid(row=0, column=0, columnspan=len(table.columns)+1)
        ttk.Label(self.central_frame, text='Ticker').grid(row=1, column=0)
        for i, col in enumerate(table.columns):
            ttk.Label(self.central_frame, text=col).grid(row=1, column=i+1)
        for y, idx in enumerate(table.index):
            ttk.Label(self.central_frame, text=idx).grid(row=2+y, column=0)
            for x, col in enumerate(table.columns):
                ttk.Label(self.central_frame, text=table.loc[idx, col]).grid(row=y+2, column=x+1)
        for x in range(len(table.index)+2):
            self.central_frame.rowconfigure(x, weight=1)
        for y in range(len(table.columns)+1):
            self.central_frame.columnconfigure(y, weight=1)


    def stats(self):
        self.clear_frame(self.central_frame)
        self.clear_radio()
        self.clear_list_box()
    
    def etf_graph(self, etf):
        self.clear_frame(self.central_frame)
        self.clear_radio()
        fig, ax = p.get_etf_by_name(self.etf_names[etf[0]]).equity_line()
        canvas = FigureCanvasTkAgg(fig, master=self.central_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.central_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.columnconfigure(0, weight=1)



def main():
    root = Tk()
    root.title('Portfolio Manager by Dodo')
    root.geometry("1400x700")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    p = Portfolio()
    main()