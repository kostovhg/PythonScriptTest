from tkinter import Tk, ttk, Frame, Label
import pandas as pd
from pandastable import Table

def displayForm(data, colWidths = None):
    
    root = Tk()
    root.title("PDF Files list")
    root.config(bg="skyblue")

    left_frame = Frame(root, width=960, height=630, bg="grey")
    left_frame.grid(row=0, column=1, padx=10, pady=5)

    right_frame = Frame(root, width=200, height=630, bg="grey")
    right_frame.grid(row=0, column=2, padx=10, pady=5)

    table_frame = Frame(left_frame, width=920, height=380, bg="red")
    table_frame.grid(row=1,column=0, padx=10, pady=5)

    tool_bar = Frame(left_frame, width=920, height=200, bg="blue")
    tool_bar.grid(row=2, column=0, padx=10, pady=5)

    Label(left_frame, text="Excel table").grid(row=0, column=0, padx=5, pady=5)

    pt = Table(table_frame, dataframe=data, width=900, maxcellwidth=3000)
    pt.show()
    if not colWidths:
        pt.columnwidths = colWidths
    
    
    root.mainloop()