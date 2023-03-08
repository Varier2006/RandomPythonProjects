# Import required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter window
win = Tk()
win.geometry("700x350")
win.title("Get the Cursor Position")

# Create an instance of style class
style = ttk.Style(win)


# Function to retrieve the current position of the cursor
def get_current_info():
    print("The cursor is at: ", entry.index(INSERT))


# Create an entry widget
entry = ttk.Entry(win, width=18)
entry.pack(pady=30)

# Create a button widget
button = ttk.Button(win, text="Get Info", command=get_current_info)
button.pack(pady=30)

win.mainloop()
