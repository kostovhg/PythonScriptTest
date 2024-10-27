import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load data from Excel
excel_path = "files.xlsx"  # Specify your Excel file path
df = pd.read_excel(excel_path)

# Create the main window
root = tk.Tk()
root.title("Editable Table")

# Create a Canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(expand=True, fill=tk.BOTH)

# Draw a rectangle on the Canvas
canvas.create_rectangle(50, 50, 550, 350, outline='black', fill='lightgrey')

# Create a Frame within the Canvas
frame = tk.Frame(canvas)
frame.place(x=50, y=50, width=500, height=300)

# Create the Treeview within the Frame
tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, minwidth=20, stretch=tk.YES)

# Insert data into the Treeview
for index, row in df.iterrows():
    tree.insert("", tk.END, values=list(row))

tree.pack(expand=True, fill=tk.BOTH)

# Function to update the pandas DataFrame with the edited data
def update_dataframe():
    for row in tree.get_children():
        values = tree.item(row)["values"]
        df.loc[int(values[0]) - 1] = values  # Assuming first column is index

# Function to handle cell double-click for editing
def edit_cell(event):
    selected_item = tree.selection()[0]
    column = tree.identify_column(event.x)
    column_index = int(column.replace("#", "")) - 1
    x, y, width, height = tree.bbox(selected_item, column)

    entry = tk.Entry(root)
    entry.place(x=x, y=y, width=width, height=height)
    entry.insert(0, tree.item(selected_item, 'values')[column_index])

    def save_edit(event):
        tree.set(selected_item, column, entry.get())
        entry.destroy()
        update_dataframe()

    entry.bind("<Return>", save_edit)
    entry.bind("<FocusOut>", lambda e: entry.destroy())

tree.bind("<Double-1>", edit_cell)

# Run the application
root.mainloop()

# Save the updated DataFrame to Excel when the window is closed
# df.to_excel("files.xlsx", index=False)
