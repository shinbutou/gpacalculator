import tkinter as tk
from tkinter import ttk


# Program Settings
system = tk.Tk()
system.title("GPA Calculator")
system.geometry("600x500")

scale = "new"

# Logic Settings
def new(p):
    p = float(p)
    if p >= 0 and p < 50:
        return 0
    elif p >= 50 and p < 60:
        return 1
    elif p >= 60 and p < 63:
        return 1.7
    elif p >= 63 and p < 67:
        return 2
    elif p >= 67 and p < 70:
        return 2.3
    elif p >= 70 and p < 73:
        return 2.7
    elif p >= 73 and p < 77:
        return 3
    elif p >= 77 and p < 80:
        return 3.3
    elif p >= 80 and p < 85:
        return 3.7
    elif p >= 85 and p < 90:
        return 4
    elif p >= 90 and p < 100:
        return 4.3
    else:
        return 0

def original(p):
    p = float(p)
    if p >= 0 and p < 50:
        return 0
    elif p >= 50 and p < 60:
        return 1
    elif p >= 60 and p < 70:
        return 2
    elif p >= 70 and p < 80:
        return 3
    elif p >= 80 and p <= 100:
        return 4


# Functions Settings
def input():
    s0 = subject.get()
    g0 = grade.get()
    c0 = credit.get()

    Ggate = False
    Cgate = False

    if g0 >= 0 and g0 <= 100:
        Ggate = True
    if c0 == 0 or 1 or 2 or 3 or 4:
        Cgate = True
        
    if Ggate and Cgate:
        combination = [s0, g0, c0]
            key = combination[0]
            value = combination[1]
            if combination[2] == "0":
                zero[key] = float(value)
            elif combination[2] == "1":
                one[key] = float(value)
            elif combination[2] == "2":
                two[key] = float(value)
            elif  combination[2] == "3":
                three[key] = float(value)
            elif combination[2] == "4":
                four[key] = float(value)

        display1.set("You've successfully input the follwoing information:\n\n"+
                     "Subject: "+str(s0)+"\n"+
                     "Grade: "+str(g0)+"\n"+
                     "Credits: "+str(c0)+"\n")
    else:
        display1.set("Something went wrong! Please check:\n\n"+
                     "Grades are restricted to values between 0 and 100.\n"+
                     "The program currently acknowledges courses rewarding up to 4 credit points only.\n\n"+
                     "Any suggestion is welcomed, contact information could be located in the [Information] tab.")

def refresh():
    display2.set("this is to refresh.")

def old_scale():
    switch = "old"
    display3.set("You've successfully switched to the mode with the previous 4 points system.")

def new_scale():
    switch = "new"
    display3.set("You've successfully switched to the mode with the current 4.3 points system.")

def calculate():
    display4.set("")

def l_import():
    display5.set("import")

def l_export():
    display5.set("export")

def help():
    display6.set("it's working now.")

def about():
    display6.set("it's working now.")


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

canvas1.place(relx=0.4, rely=0.05)
canvas2.place(relx=0.4, rely=0.05)
canvas3.place(relx=0.4, rely=0.05)
canvas4.place(relx=0.4, rely=0.05)
canvas5.place(relx=0.4, rely=0.05)
canvas6.place(relx=0.4, rely=0.05)


# [Input Data] Settings
subject = tk.StringVar()
grade = tk.DoubleVar()
credit = tk.IntVar()

lb1a1 = tk.Label(tab1, text = "Subject:")
et1a1 = tk.Entry(tab1, textvariable = subject)
lb1b1 = tk.Label(tab1, text = "Grade:")
et1b1 = tk.Entry(tab1, textvariable = grade)
lb1c1 = tk.Label(tab1, text = "Credit:")
et1c1 = tk.Entry(tab1, textvariable = credit)
fn1b1 = tk.Button(tab1, height = 2, width = 11, text = "Enter", command = input)

lb1a1.place(relx = 0.05, rely = 0.05)
et1a1.place(relx = 0.05, rely = 0.1)
lb1b1.place(relx = 0.05, rely = 0.18)
et1b1.place(relx = 0.05, rely = 0.23)
lb1c1.place(relx = 0.05, rely = 0.31)
et1c1.place(relx = 0.05, rely = 0.36)
fn1b1.place(relx = 0.05, rely = 0.5)



# [View Input] Settings
tb2_message = tk.Label(tab2, text = "Click to update the information:")
bt2_refresh = tk.Button(tab2, height = 2, width = 11, text = "Refresh")

tb2_message.place(relx = 0.05, rely = 0.05)
bt2_refresh.place(relx = 0.05, rely = 0.2)


# [Scale Switch] Settings
tb3_message = tk.Label(tab3, text = "GPA Scale:")
bt3_four = tk.Button(tab3, text = "4", height = 3, width = 6, command = old_scale)
bt3_fp3 = tk.Button(tab3, text = "4.3", height = 3, width = 6, command = new_scale)

tb3_message.place(relx = 0.05, rely = 0.05)
bt3_four.place(relx = 0.05, rely = 0.15)
bt3_fp3.place(relx = 0.15, rely = 0.15)


# [Calculation] Settings
tb4_message = tk.Label(tab4, text = "Based on current input:")     
bt4_calculate = tk.Button(tab4, height = 2, width = 11, text = "Calculate", command = calculate)

tb4_message.place(relx = 0.05, rely = 0.05)
bt4_calculate.place(relx = 0.05, rely = 0.2)


# [Import/Export Data] Settings
tb5_message = tk.Label(tab5, text = "Functions:") 
bt5_import = tk.Button(tab5, height = 2, width = 11, text = "Import", command = l_import)
bt5_export = tk.Button(tab5, height = 2, width = 11, text = "Export", command = l_export)

tb5_message.place(relx = 0.05, rely = 0.05)
bt5_import.place(relx = 0.05, rely = 0.15)
bt5_export.place(relx = 0.05, rely = 0.25)


# [Information] Settings
tb6_message = tk.Label(tab6, text = "Functions:") 
bt6_help = tk.Button(tab6, height = 2, width = 11, text = "Help", command = help)
bt6_about = tk.Button(tab6, height = 2, width = 11, text = "About", command = about)

tb6_message.place(relx = 0.05, rely = 0.05)
bt6_help.place(relx = 0.05, rely = 0.15)
bt6_about.place(relx = 0.05, rely = 0.25)


system.mainloop()