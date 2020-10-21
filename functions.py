from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *


def graph(fig, frame):
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()