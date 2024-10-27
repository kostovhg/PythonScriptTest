
# This file was generated by the tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/tkinter-Designer

import sys
sys.path.append(r'C:\Users\uKBo\OneDrive\Documents\PythonScriptTest')
import addtext as at
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\uKBo\OneDrive\Documents\PythonScriptTest\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1120x860")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 860,
    width = 1120,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
#This should be the list
df = at.read_excel(r'C:\Users\uKBo\OneDrive\Documents\PythonScriptTest\files.xlsx')
canvas.create_rectangle(
    95.0,
    205.0,
    455.0,
    747.0,
    fill="pink",
    outline="")
#Create a Frame within the canvas
frame = ttk.Frame(canvas, relief="ridge", borderwidth=1)
frame.pack(padx=10, pady=10, fill="both", expand=True)
tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")
# Create the Treeview withing the frame
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, minwidth = 100)
#insert data into the treeview
for index, row in df.iterrows():
    tree.insert('', tk.END, values=list(row))

tree.pack(expand=True, fill='both')

canvas.create_text(
    111.0,
    96.0,
    anchor="nw",
    text="Project number",
    fill="#000000",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_text(
    111.0,
    181.0,
    anchor="nw",
    text="Code",
    fill="#000000",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_text(
    207.0,
    181.0,
    anchor="nw",
    text="Count",
    fill="#000000",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_text(
    273.0,
    181.0,
    anchor="nw",
    text="Has bend",
    fill="brown",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_text(
    377.0,
    181.0,
    anchor="nw",
    text="Included",
    fill="yellow",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1104.0,
    80.0,
    fill="#97C6EC",
    outline="")

canvas.create_text(
    207.0,
    30.0,
    anchor="nw",
    text="List of drawings from table:",
    fill="#000000",
    font=("RobotoRoman Regular", 16 * -1)
)

canvas.create_text(
    114.0,
    151.0,
    anchor="nw",
    text="Increase/decrase quantity",
    fill="#000000",
    font=("RobotoRoman Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=314.0,
    y=751.0,
    width=121.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=95.0,
    y=751.0,
    width=148.0,
    height=40.0
)

# Here will be the commond count denominator
canvas.create_rectangle(
    332.0,
    144.0,
    364.0,
    176.0,
    fill="grey",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=399.0,
    y=151.0,
    width=22.0,
    height=19.0
)

canvas.create_rectangle(
    231.0,
    91.0,
    416.0,
    123.0,
    fill="blue",
    outline="")

canvas.create_rectangle(
    427.0,
    25.0,
    943.0,
    57.0,
    fill="green",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=984.0,
    y=23.0,
    width=81.0,
    height=40.0
)

canvas.create_rectangle(
    489.0,
    116.0,
    1059.0,
    670.0,
    fill="#B8DAEA",
    outline="")
window.resizable(False, False)

#at.display_table(at.read_excel(r'C:\Users\uKBo\OneDrive\Documents\PythonScriptTest\files.xlsx'))
window.mainloop()