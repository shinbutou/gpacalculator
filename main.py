import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext


# Program Settings
system = tk.Tk()
system.title("GPA Calculator")
system.geometry("625x525")


#Initialization
scale_switch = "old"
zero = dict()
one = dict()
two = dict()
three = dict()
four = dict()
czero = dict()
cone = dict()
ctwo = dict()
cthree = dict()
cfour = dict()


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

def old(p):
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
    sinput = subject.get()
    ginput = grade.get()
    cinput = credit.get()

    Sgate = False
    Ggate = False
    Cgate = False
    
    if sinput != "":
        Sgate = True
    if ginput >= 0 and ginput <= 100:
        Ggate = True
    if cinput == 0 or 1 or 2 or 3 or 4:
        Cgate = True
        
    if Ggate and Cgate and Sgate:
        combination = [str(sinput), str(ginput), str(cinput)]
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
                     "Subject: "+str(sinput)+"\n"+
                     "Grade: "+str(ginput)+"\n"+
                     "Credits: "+str(cinput)+"\n")
    else:
        display1.set("Something went wrong! Please check:\n\n"+
                     "Grades are restricted to values between 0 and 100.\n"+
                     "The program currently acknowledges courses rewarding up to 4 credit points only.\n\n"+
                     "Any suggestion is welcomed, contact information could be located in the information tab.")


def refresh():
    showcase.delete(1.0, END)
    for x, y in three.items():
        showcase.insert(END, str(x)+": "+str(y)+", 3 credit points\n")
    for x, y in two.items():
        showcase.insert(END, str(x)+": "+str(y)+", 2 credit points\n")
    for x, y in one.items():
        showcase.insert(END, str(x)+": "+str(y)+", 1 credit points\n")
    for x, y in zero.items():
        showcase.insert(END, str(x)+": "+str(y)+", 0 credit points\n")
    for x, y in four.items():
        showcase.insert(END, str(x)+": "+str(y)+", 4 credit points\n")
    

def old_scale():
    global scale_switch
    scale_switch = "old"
    display3.set("You've successfully switched to the mode of the previous 4 points system.")


def new_scale():
    global scale_switch
    scale_switch = "new"
    display3.set("You've successfully switched to the mode of the current 4.3 points system.")


def calculate():
    credit_sum = len(zero)*0 + len(one)*1 + len(two)*2 + len(three)*3 + len(four)*4
    course_count = len(zero) + len(one) + len(two) + len(three) + len(four)

    
    czero = zero.copy()
    cone = one.copy()
    ctwo = two.copy()
    cthree = three.copy()
    cfour = four.copy()

    if course_count != 0:
        if scale_switch == "new":
            for x,y in czero.items():
                czero[x] = new(y)
            for x,y in cone.items():
                cone[x] = new(y)
            for x,y in ctwo.items():
                ctwo[x] = new(y)
            for x,y in cthree.items():
                cthree[x] = new(y)
            for x,y in cfour.items():
                cfour[x] = new(y)
        elif scale_switch == "old":
            for x,y in czero.items():
                czero[x] = old(y)
            for x,y in cone.items():
                cone[x] = old(y)
            for x,y in ctwo.items():
                ctwo[x] = old(y)
            for x,y in cthree.items():
                cthree[x] = old(y)
            for x,y in cfour.items():
                cfour[x] = old(y)
    else:
        display4.set("Please input data before calculation.")

    zero_sum = sum(zero.values())
    one_sum = sum(one.values())
    two_sum = sum(two.values())
    three_sum = sum(three.values())
    four_sum = sum(four.values())
    czero_sum = sum(czero.values())
    cone_sum = sum(cone.values())
    ctwo_sum = sum(ctwo.values())
    cthree_sum = sum(cthree.values())
    cfour_sum = sum(cfour.values())

    grand_sum = zero_sum*0 + one_sum*1 + two_sum*2 + three_sum*3 + four_sum*4
    cgrand_sum = czero_sum*0 + cone_sum*1 + ctwo_sum*2 + cthree_sum*3 + cfour_sum*4
    
    if credit_sum != 0:
        average = float(grand_sum/credit_sum)
        gpa = float(cgrand_sum/credit_sum)
    else:
        score = 0
        gpa = 0
    
    display4.set("According to the input data, calculated:\n\n"+
                 "Credits Acquired: "+str(credit_sum)+"\n"+
                 "Overall Average: "+str(round(average, 2))+"\n"+
                 "Overall GPA: "+str(round(gpa, 2)))


def l_import():
    zero.clear()
    one.clear()
    two.clear()
    three.clear()
    four.clear()

    with open("database.csv", newline="") as csvfile:
        rows = csv.reader(csvfile, delimiter = ";")
        for row in rows:
            if row[0] == "0":
                zero[str(row[1])] = float(row[2])
            elif row[0] == "1":
                one[str(row[1])] = float(row[2])
            elif row[0] == "2":
                two[str(row[1])] = float(row[2])
            elif row[0] == "3":
                three[str(row[1])] = float(row[2])
            elif row[0] == "4":
                four[str(row[1])] = float(row[2])

    display5.set("Successfully imported data from database.txt in same directory.")


def l_export():
    database = open("database.csv", "w+", encoding="utf-8")
    database.write("gpa_calculator_database")
    for x,y in zero.items():
        database.write("\n0;"+x+";"+str(y))
    for x,y in one.items():
        database.write("\n1;"+x+";"+str(y))
    for x,y in two.items():
        database.write("\n2;"+x+";"+str(y))
    for x,y in three.items():
        database.write("\n3;"+x+";"+str(y))
    for x,y in four.items():
        database.write("\n4;"+x+";"+str(y))
    database.close()

    display5.set("Successfully exported an importable file in the same directory for future updates.")


def guide():
    display6.set("*The standand procedure is listed below:\n\n"+
                 "1. Input or import data.\n"+
                 "2. Check the data. (optional)\n"+
                 "3. Choose the preferable GPA scale. (optional)\n"+
                 "4. Calculate indices, including overall GPA.\n"+
                 "5. Export data for future updates. (optional)\n\n\n"+
                 "- "*30+"\n\n"+
                 "*Store the file in confinement for your privacy.\n\n"+
                 "- "*30+"\n\n"+
                 "*To import data, the file should be placed in the same directory as the program itself.")


def about():
    display6.set("The GPA Calculator program was designed to provide an intuitive measure to catalog "+
                 "and calculate the crucial indices for students of National Chengchi University.\n\n"+
                 "For problem reporting and feature suggestion, you would be able to reach the developer "+
                 "through the university email address (106308049).")


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

canvas1.place(relx=0.05, rely=0.05)
canvas2.place(relx=0.05, rely=0.05)
canvas3.place(relx=0.05, rely=0.05)
canvas4.place(relx=0.05, rely=0.05)
canvas5.place(relx=0.05, rely=0.05)
canvas6.place(relx=0.05, rely=0.05)


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

lb1a1.place(relx = 0.6, rely = 0.06)
et1a1.place(relx = 0.6, rely = 0.11)
lb1b1.place(relx = 0.6, rely = 0.19)
et1b1.place(relx = 0.6, rely = 0.24)
lb1c1.place(relx = 0.6, rely = 0.32)
et1c1.place(relx = 0.6, rely = 0.37)
fn1b1.place(relx = 0.6, rely = 0.51)



# [View Input] Settings
tb2_message = tk.Label(tab2, text = "Click to update the information:")
bt2_refresh = tk.Button(tab2, height = 2, width = 11, text = "Refresh", command = refresh)
showcase = scrolledtext.ScrolledText(tab2, wrap = tk.WORD, width = 68, height = 20)

tb2_message.place(relx = 0.6, rely = 0.05)
bt2_refresh.place(relx = 0.6, rely = 0.11)
showcase.place(relx=0.05, rely=0.25)


# [Scale Switch] Settings
tb3_message = tk.Label(tab3, text = "GPA Scale:")
bt3_four = tk.Button(tab3, text = "4", height = 3, width = 6, command = old_scale)
bt3_fp3 = tk.Button(tab3, text = "4.3", height = 3, width = 6, command = new_scale)

tb3_message.place(relx = 0.6, rely = 0.05)
bt3_four.place(relx = 0.6, rely = 0.11)
bt3_fp3.place(relx = 0.74, rely = 0.11)


# [Calculation] Settings
tb4_message = tk.Label(tab4, text = "Based on current input:")     
bt4_calculate = tk.Button(tab4, height = 2, width = 11, text = "Calculate", command = calculate)

tb4_message.place(relx = 0.6, rely = 0.05)
bt4_calculate.place(relx = 0.6, rely = 0.11)


# [Import/Export Data] Settings
tb5_message = tk.Label(tab5, text = "Functions:") 
bt5_import = tk.Button(tab5, height = 2, width = 11, text = "Import", command = l_import)
bt5_export = tk.Button(tab5, height = 2, width = 11, text = "Export", command = l_export)

tb5_message.place(relx = 0.6, rely = 0.05)
bt5_import.place(relx = 0.6, rely = 0.11)
bt5_export.place(relx = 0.6, rely = 0.23)


# [Information] Settings
tb6_message = tk.Label(tab6, text = "Functions:") 
bt6_help = tk.Button(tab6, height = 2, width = 11, text = "Help", command = guide)
bt6_about = tk.Button(tab6, height = 2, width = 11, text = "About", command = about)

tb6_message.place(relx = 0.6, rely = 0.05)
bt6_help.place(relx = 0.6, rely = 0.11)
bt6_about.place(relx = 0.6, rely = 0.23)


system.mainloop()
