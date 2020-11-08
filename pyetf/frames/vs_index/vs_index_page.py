from tkinter import *
from tkinter import ttk
from tkinter import font
from pyetf.functions import configure, graph, date_to_text, date_from_text

class VsIndexPage:
    """Class representing the page where you can confront your portfolio against other index"""

    indexToTicker = {'S&P 500': 'SPY', 'NASDAQ': '^IXIC', 'DAX': '^GDAXI', 'DOW JONES': '^DJI', 'NIKKEI 225': '^N225', 'FTSE MIB': 'FTSEMIB.MI'}

    def __init__(self, app):
        """
        Initialization of the page.
        """
        titleFont = font.Font(family='Helvetica', name='titleFont', size=17)
        titleStyle = ttk.Style()
        titleStyle.configure('TitleVsIndex.TLabel', foreground='#2464e3', font=titleFont)

        self.app = app
        self.portfolio = app.p

        self.centralFrame = ttk.Frame(app.mainframe)

        self.left_frame_init()
        self.leftFrame.grid(row=0, column=0, sticky=(W, N, S, E), padx=15)

        ttk.Separator(app.mainframe, orient=VERTICAL).grid(row=0, column=1, sticky='nswe')
        self.centralFrame.grid(row=0, column=2, columnspan=5, sticky=(E, W, N, S), padx=15)

        ttk.Separator(app.mainframe, orient=VERTICAL).grid(row=0, column=7, sticky='nswe')

        self.right_frame_init()
        self.rightFrame.grid(row=0, column=8, columnspan=2, sticky=(E, N, S, W), padx=15)

        configure(app.mainframe, 1, 8)

        self.equity_graph(index='SPY')
    
    def left_frame_init(self):
        """
        Initialization of the left frame.
        :return None
        """
        self.leftFrame = ttk.Frame(self.app.mainframe)

        # Selezione Indice --> Combobox e Label
        ttk.Label(self.leftFrame, text='Portafoglio vs', justify='center', style='TitleVsIndex.TLabel').grid(row=0, column=0, columnspan=2, pady=(20,0))
        self.index = StringVar(value='S&P 500')
        self.combo = ttk.Combobox(self.leftFrame, textvariable=self.index, width=14, justify='center', state='readonly', values=list(self.indexToTicker.keys()))
        self.combo.option_add('*TCombobox*Listbox.Justify', 'center')
        self.combo.grid(row=1, column=0, columnspan=2, pady=(0,20))
        self.combo.bind('<<ComboboxSelected>>', lambda _: self.combo.selection_clear())

        # Separator
        ttk.Separator(self.leftFrame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=2, sticky='nswe', padx=(20, 0))

        # Data Iniziale --> Entry e Label
        ttk.Label(self.leftFrame, text="Data iniziale").grid(row=3, column=0)
        dIni = self.portfolio.data.index[0]
        self.dateIni = StringVar(value=date_to_text(dIni))
        ttk.Entry(self.leftFrame, textvariable=self.dateIni, width=10, justify='center').grid(row=3, column=1)

        # Bottone per rimettere il primo giorno --> Button
        ttk.Button(self.leftFrame, text='Inizio', command=lambda: self.dateIni.set(date_to_text(dIni))).grid(row=4, column=0, columnspan=2, pady=(0,20))

        # Data Finale --> Entry e Label
        ttk.Label(self.leftFrame, text="Data finale").grid(row=5, column=0, pady=(20,0))
        dFin = self.portfolio.data.index[-1]
        self.dateFin = StringVar(value=date_to_text(dFin))
        ttk.Entry(self.leftFrame, textvariable=self.dateFin, width=10, justify='center').grid(row=5, column=1, pady=(20,0))

        # Bottone per rimettere l'ultimo giorno --> Button
        ttk.Button(self.leftFrame, text='Fine', command=lambda: self.dateFin.set(date_to_text(dFin))).grid(row=6, column=0, columnspan=2)

        # Separator
        ttk.Separator(self.leftFrame, orient=HORIZONTAL).grid(row=7, column=0, columnspan=2, sticky='nswe', padx=(20, 0))
        
        # Bottone per aggiornare --> Button
        ttk.Button(self.leftFrame, text='Aggiorna', command=self.refresh_page).grid(row=8, column=0, columnspan=2, pady=(0,30))

        configure(self.leftFrame, 9, 2)
    
    def right_frame_init(self):
        """
        Initialization of the right frame.
        :return None
        """
        self.rightFrame = ttk.Frame(self.app.mainframe)

        pPerformance, idxPerfomance, comparedPerfomance = self.portfolio.performance_vs_index() # Initial Stats

        # Statistiche --> Labels
        ttk.Label(self.rightFrame, text='Statistiche', anchor='s', style='TitleVsIndex.TLabel').grid(row=0, column=0, columnspan=2, pady=(20,0))
        
        dateIni = date_to_text(self.portfolio.data.index[0], True)
        dateFin = date_to_text(self.portfolio.data.index[-1], True)
        self.dates = ttk.Label(self.rightFrame, text=f'{dateIni}\n-\n{dateFin}', justify='center')
        self.dates.grid(row=1, column=0, columnspan=2)

        ttk.Label(self.rightFrame, text='Performance del\nPortafoglio', justify='center').grid(row=2, column=0, padx=10)
        self.portfolioPerformance = ttk.Label(self.rightFrame, text=format(pPerformance, '.2f') + ' %')
        self.portfolioPerformance.grid(row=2, column=1, padx=10)

        self.l1 = ttk.Label(self.rightFrame, text=f'Performance \n{self.index.get()}', justify='center')
        self.l1.grid(row=3, column=0, padx=10)
        self.indexPerformance = ttk.Label(self.rightFrame, text=format(idxPerfomance, '.2f') + ' %')
        self.indexPerformance.grid(row=3, column=1, padx=10)

        self.l2 = ttk.Label(self.rightFrame, text=f'Portafoglio\nvs\n{self.index.get()}', justify='center')
        self.l2.grid(row=4, column=0, padx=10)
        self.comparedPerformance = ttk.Label(self.rightFrame, text=format(comparedPerfomance, '.2f') + ' %')
        self.comparedPerformance.grid(row=4, column=1, padx=10)

        # Separator
        ttk.Separator(self.rightFrame, orient=HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky='nswe', padx=(20, 0))


        # Bottone per tornare alla pagina iniziale --> Button
        ttk.Button(self.rightFrame, text='Pagina Iniziale', command=self.app.initial_page).grid(row=6, column=0, columnspan=2)

        # Bottone per chiudere l'applicazione --> Button
        ttk.Button(self.rightFrame, text='Chiudi', command=self.app.mainframe.quit).grid(row=7, column=0, columnspan=2)
        
        configure(self.rightFrame, 8, 1)

    def equity_graph(self, **kwargs):
        """
        Draws the equity graph on the central frame based on the arguments passed as parameters.
        :param kwargs: dict
        :return None
        """
        self.centralFrame = ttk.Frame(self.app.mainframe)
        self.centralFrame.grid(row=0, column=2, columnspan=5, sticky=(E, W, N, S), padx=15)
        #clear_selection('PortfolioGraphs', self)
        fig, ax = self.portfolio.equity_line(pct=True, **kwargs)
        # frame = ttk.Frame(self.c_frame)
        # frame.pack(side=BOTTOM)
        # ttk.Checkbutton(frame, text='Percentuale', variable=pct, onvalue=True, offvalue=False, command=lambda: self.equity_graph(pct=pct.get(), sp500=sp500.get())).grid(row=0, column=0, pady=20, padx=20)
        # ttk.Checkbutton(frame, text='S&P500', variable=sp500, onvalue=True, offvalue=False, command=lambda: self.equity_graph(pct=pct.get(), sp500=sp500.get())).grid(row=0, column=2, pady=20, padx=20)
        # configure(frame, 0, 3)
        graph(fig, self.centralFrame)
    
    def refresh_page(self):
        """
        Refresh the vsIndex page considering the parameters chosen by the user.
        :return None
        """
        iniChoice = date_from_text(self.dateIni.get())
        finChioce = date_from_text(self.dateFin.get())
        idxChoice = self.indexToTicker[self.index.get()]
        self.equity_graph(index=idxChoice, dateIni=iniChoice, dateFin=finChioce)
        pPerformance, idxPerfomance, comparedPerfomance = self.portfolio.performance_vs_index(idxChoice, iniChoice, finChioce)
        self.portfolioPerformance['text'] = format(pPerformance, '.2f') + ' %'
        self.indexPerformance['text'] = format(idxPerfomance, '.2f') + ' %'
        self.comparedPerformance['text'] = format(comparedPerfomance, '.2f') + ' %'
        self.l1['text'] = f'Performance \n{self.index.get()}'
        self.l2['text'] = f'Portafoglio\nvs\n{self.index.get()}'
        self.dates['text'] = f'{date_to_text(iniChoice, True)}\n-\n{date_to_text(finChioce, True)}'
