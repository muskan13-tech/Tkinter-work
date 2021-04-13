import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("TAB Control")

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1 , text="Page 1")
nb.add(page2 , text="Page 2")

nb.pack(expand=True , fill = "both")

label1 = ttk.Label(page1 , text = "This is 1st page : ")
label1.grid(row = 0,column = 0)

label2 = ttk.Label(page2 , text = "This is 2nd page : ")
label2.grid(row = 0,column = 0)

win.mainloop()