import tkinter as tk 
from tkinter import ttk 
win = tk.Tk()
win.title("Menubar")

# menu 
def func():
    print("Function is called .")

# menu 
main_menu = tk.Menu(win)

# file column 
file_menu = tk.Menu(main_menu,tearoff = 0)
file_menu.add_command(label = "New File" , command = func)
file_menu.add_command(label = "New Window" , command = func)
file_menu.add_separator()
file_menu.add_command(label = "Save" , command = func)
file_menu.add_command(label = "Save As" , command = func)
file_menu.add_command(label = "Save All" , command = func)
file_menu.add_separator()
file_menu.add_command(label = "Close Editor" , command = func)
file_menu.add_command(label = "Exit" , command = func)

# edit column
edit_menu = tk.Menu(main_menu,tearoff = 0)
edit_menu.add_command(label = "Undo" , command = func)
edit_menu.add_command(label = "Redo" , command = func)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut" , command = func)
edit_menu.add_command(label = "Copy" , command = func)
edit_menu.add_command(label = "Paste" , command = func)
edit_menu.add_command(label = "Copy As" , command = func)
edit_menu.add_separator()
edit_menu.add_command(label = "Find" , command = func)
edit_menu.add_command(label = "Replace" , command = func)

# run
run_menu = tk.Menu(main_menu,tearoff=0)
run_menu.add_command(label = "Compile" , command = func)
run_menu.add_command(label = "Compile & Run" , command = func)
run_menu.add_command(label = "Run" , command = func)



# adding to main 
main_menu.add_cascade(label = 'File' , menu = file_menu)
main_menu.add_cascade(label = "Edit" , menu = edit_menu)
main_menu.add_cascade(label = 'Run', menu = run_menu)

win.config(menu = main_menu)

win.mainloop()