# starting code.

import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os      #for ignoring extra spaces.
win = tk.Tk()
win.title("GUI_APP")


# create a label.

name_label = ttk.Label(win,text="Enter your name : ")
name_label.grid(row=0,column=0,sticky=tk.W)

age_label = ttk.Label(win,text="Enter your age : ")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label = ttk.Label(win,text="Enter your email : ")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text="Select your gender ")
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry boxes for the labels.
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width = 16 , textvariable = name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var = tk.IntVar()
age_entrybox = ttk.Entry(win,width = 16 , textvariable = age_var)
age_entrybox.grid(row=1,column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width = 16 , textvariable = email_var)
email_entrybox.grid(row=2,column=1)


# create radio button 
usertype = tk.StringVar()
radio_1 = ttk.Radiobutton(win, text = "Student" , value = "Student" , variable=usertype).grid(row=4,column=0)

radio_2 = ttk.Radiobutton(win, text = "Teacher" , value = "Teacher" , variable=usertype).grid(row=4,column=1)

radio_3 = ttk.Radiobutton(win, text = "Parent" , value = "Parent" , variable=usertype).grid(row=4,column=2)


# create checkbox

chckbtn_var = tk.IntVar()
chck_btn = ttk.Checkbutton(win,text="Terms and conditions" , variable=chckbtn_var).grid(row=5,columnspan=3)

# create combo box to select the options.

gender_var = tk.StringVar()
gender_combo=ttk.Combobox(win,width = 14, textvariable = gender_var , state="readonly" )
gender_combo['values'] = ("Select your options","Male","Female","Other")
gender_combo.current(0)
gender_combo.grid(row=6,column=1)


# create a button and perform its working .
def action():
    username = name_var.get()
    userage = age_var.get()
    email = email_var.get()
    print(f"{username} has an age of {userage} having email id {email} .")
    usergender = gender_var.get()
    user_type=usertype.get()
    if chckbtn_var.get() == 0:
        subscriped = "NO"
    else:
        subscriped = "YES"    
    print(usergender , user_type , subscriped)
    

    with open("file.csv",'a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames = ['Name' , 'Age' ,'Email','Gender','Type','T&C'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Name' : username,
            'Age': userage,
            'Email' : email,
            'Gender': usergender,
            'Type': user_type,
            'T&C': subscriped
        })

    
    # to delete the corresponding values 
    name_entrybox.delete(0,tk.END) 
    age_entrybox.delete(0,tk.END) 
    email_entrybox.delete(0,tk.END) 

submit_button = ttk.Button(win,text = "Submit", command=action).grid(row=7,column=0)

win.mainloop()