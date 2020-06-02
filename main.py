import tkinter as tk
from tkinter import ttk


# Program Settings
system = tk.Tk()
system.title("GPA Calculator")
system.geometry("600x500")


# Tab Settings
tab_parent = ttk.Notebook(system)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text = "Input Data")
tab_parent.add(tab2, text = "View Input")
tab_parent.add(tab3, text = "Scale Switch")
tab_parent.add(tab4, text = "Calculation")
tab_parent.add(tab5, text = "Import/Export Data")
tab_parent.add(tab6, text = "Information")
tab_parent.pack(expand = 1, fill = "both")
    
# Displays Settings
display1 = tk.StringVar()
display2 = tk.StringVar()
display3 = tk.StringVar()
display4 = tk.StringVar()
display5 = tk.StringVar()
display6 = tk.StringVar()

display1.set("Here's where you input data, specifying the name of the course, credit points and grade received.")
display2.set("Here's where you view the input data. The editing function is still under development.")
display3.set("Here's where you switch between the grade point average scale of 4 (old) and 4.3 (new).")
display4.set("Here's where you execute the process of calculation and generate the result.")
display5.set("Here's where you export a readable data for future updates or import the previous data.")
display6.set("Here's where you can find more information about this program.")

canvas1 = tk.Message(tab1, textvariable = display1, width = 300)
canvas2 = tk.Message(tab2, textvariable = display2, width = 300)
canvas3 = tk.Message(tab3, textvariable = display3, width = 300)
canvas4 = tk.Message(tab4, textvariable = display4, width = 300)
canvas5 = tk.Message(tab5, textvariable = display5, width = 300)
canvas6 = tk.Message(tab6, textvariable = display6, width = 300)

canvas1.place(relx=0.55, rely=0.05)
canvas2.place(relx=0.55, rely=0.05)
canvas3.place(relx=0.55, rely=0.05)
canvas4.place(relx=0.55, rely=0.05)
canvas5.place(relx=0.55, rely=0.05)
canvas6.place(relx=0.55, rely=0.05)


# [Input Data] Settings
subject = 0
grade = 0
credit = 0
    
lb1a1 = tk.Label(tab1, text = "Subject:")
et1a1 = tk.Entry(tab1, textvariable = subject)
lb1b1 = tk.Label(tab1, text = "Grade:")
et1b1 = tk.Entry(tab1, textvariable = grade)
lb1c1 = tk.Label(tab1, text = "Credit:")
et1c1 = tk.Entry(tab1, textvariable = credit)
fn1b1 = tk.Button(tab1, height = 1, width = 10, text = "Enter")

lb1a1.place(relx = 0.05, rely = 0.22)
et1a1.place(relx = 0.05, rely = 0.27)
lb1b1.place(relx = 0.05, rely = 0.35)
et1b1.place(relx = 0.05, rely = 0.40)
lb1c1.place(relx = 0.05, rely = 0.48)
et1c1.place(relx = 0.05, rely = 0.53)
fn1b1.place(relx = 0.12, rely = 0.75)



# [View Input] Settings
fn2_message = tk.Label(tab2, text = "Do you want to refresh?", fg='blue')
fn2a1 = tk.Button(tab2, height = 1, width = 10, text = "Refresh", bg='blue', fg='white')
fn2_message.place(relx = 0.10, rely = 0.12)
fn2a1.place(relx = 0.12, rely = 0.75)


# [Scale Switch] Settings


# [Calculation] Settings    
fn4_message = tk.Label(tab4, text = "Do you finish entering all of the entry?", fg = 'orangered') 
fn4a0 = tk.Button(tab4, height = 1, width = 10, text = "Calculate", bg = 'firebrick')
fn4_message.place(relx = 0.10, rely = 0.12)
fn4a0.place(relx = 0.12, rely = 0.75)


# [Import/Export Data] Settings
fn5_import = tk.Button(tab5, height = 3, width = 11, text = "Import")
fn5_export = tk.Button(tab5, height = 3, width = 11, text = "Export")

fn5_import.place(relx = 0.05, rely = 0.75)
fn5_export.place(relx = 0.25, rely = 0.75)


# [Information] Settings
fn6_help = tk.Button(tab6, height = 3, width = 12, text = "Help")
fn6_about = tk.Button(tab6, height = 3, width = 12, text = "About")

fn6_help.place(relx = 0.05, rely = 0.75)
fn6_about.place(relx = 0.25, rely = 0.75)


system.mainloop()