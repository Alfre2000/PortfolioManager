from tkinter import *
from tkinter import ttk
from portfolio import Portfolio
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Frames.right_frame import RightFrame
from functions import clear_frame



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
        self.right_frame = RightFrame(self.mainframe, self, p)
        self.right_frame.grid(row=0, column=6, sticky=(E, N, S, W), padx=15)
        
        self.last_day()

    def last_day(self):
        clear_frame(self.central_frame)
        self.clear_radio()
        self.right_frame.etf_list.clear_box()
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
    
    def clear_radio(self):
        self.equityGraph.state(['!selected'])
        self.valueGraph.state(['!selected'])
        self.investedGraph.state(['!selected'])
        self.barGraph.state(['!selected'])
        self.pieGraph.state(['!selected'])
        self.investmentTable.state(['!selected'])
        self.portfolioTable.state(['!selected'])
    
    def value_line(self):
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.right_frame.etf_list.clear_box()
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
        clear_frame(self.central_frame)
        self.clear_radio()
        self.right_frame.etf_list.clear_box()


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