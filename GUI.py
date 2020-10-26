from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from portfolio import Portfolio
from Frames.right_frame import RightFrame
from Frames.left_frame import LeftFrame
from functions import *


class App:

    def __init__(self, root):
        # s = ttk.Style()
        # s.configure('Frame1.TFrame', background='red')

        self.p = Portfolio()
        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


        self.central_frame = ttk.Frame(self.mainframe)

        self.left_frame = LeftFrame(self.mainframe, self)
        self.left_frame.grid(row=0, column=0, sticky=(W, N, S, E), padx=15)

        ttk.Separator(self.mainframe, orient=VERTICAL).grid(row=0, column=1, sticky='nswe')
        self.central_frame.grid(row=0, column=2, columnspan=5, sticky=(E, W, N, S), padx=15)

        ttk.Separator(self.mainframe, orient=VERTICAL).grid(row=0, column=7, sticky='nswe')

        self.right_frame = RightFrame(self.mainframe, self)
        self.right_frame.grid(row=0, column=8, columnspan=2, sticky=(E, N, S, W), padx=15)

        self.menu = Menu(root)
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(menu=self.fileMenu, label='File')
        self.fileMenu.add_command(label='Open...', command=self.openFile)
        root['menu'] = self.menu

        configure(self.mainframe, 1, 8)
        
        self.left_frame.last_day()

    def new_central_frame(self):
        """
        Creates a new central frame in order to be able to show new things on it.
        :reeturn ttk.Frame
        """
        self.central_frame.destroy()
        self.central_frame = ttk.Frame(self.mainframe)
        self.central_frame.grid(row=0, column=2, columnspan=5, sticky=(E, W, N, S), padx=15)
        return self.central_frame
    
    def openFile(self):
        """
        Change the Info file for the portfolio.
        :return None
        """
        filename = filedialog.askopenfilename()
        self.p = Portfolio(filename)
        self.left_frame.p = self.p
        self.right_frame.p = self.p
        self.right_frame.etf_list.p = self.p
        self.right_frame.etf_list.refresh()
        self.right_frame.add_etf.p = self.p
        self.right_frame.sell_etf.p = self.p
        self.left_frame.last_day()

def main():
    root = Tk()
    root.title('Portfolio Manager by Dodo')
    root.geometry("1400x700+20+80")
    root.option_add('*tearOff', FALSE)
    img = PhotoImage(file='Images/Icon.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()