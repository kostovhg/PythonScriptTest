from tkinter import *

root = Tk()
root.title("Basic GUI Layout")
root.maxsize(900, 600)
root.config(bg="skyblue")

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg="grey")
left_frame.grid(row=0, column=0, padx=10, pady=2)

right_frame = Frame(root, width=650, height=400, bg="grey")
right_frame.grid(row=0, column=1, padx=10, pady=2)

# Create frames and labesl in left_frame
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# Load image to be "edited"
# image = PhotoImage(file=r"C:\Users\uKBo\OneDrive\Pictures\pikachu.png")
# original_image = image.subsample(4, 4) # Resize image using subsample
# Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# Display image in right_frame
# Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10) # ipadx=10 - padding innside the label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=4, column=1, padx=5, pady=5)

root.mainloop()