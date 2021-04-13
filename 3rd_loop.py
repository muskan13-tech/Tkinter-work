# import tkinter 

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("LOOP")

# create label

labels = ['what is your name : ','what is your age : ','what is your gender : ','what is your email id : ','City : ']

for i in range(len(labels)):      # loop has introduced 
    cur_label = ttk.Label(text = labels[i])
    cur_label.grid(row=i,column = 0 , padx = 40 , pady = 5)  #padding include 

#Entry box
var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age':tk.StringVar(),
    'gender': tk.StringVar(),
    'email': tk.StringVar(),
    'city': tk.StringVar()
}
counter = 0
for i in user_info:
    cur_var = ttk.Entry(win , width = 16 , textvariable = user_info[i])
    cur_var.grid(row=counter,column = 1, padx=40 , pady = 5)
    counter += 1 

# button
def submit():
    for i in  user_info:
        print(user_info[i].get())


sub_btn = ttk.Button(win , text="Submit", command = submit).grid(row = 6 , columnspan = 3)

win.mainloop()

