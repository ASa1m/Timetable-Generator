import random
from tkinter import *
from tkinter import messagebox,ttk
import datetime
from copy import deepcopy
import csv
from datetime import datetime, date, time, timedelta

############# Predefined values and instructons ###############

header = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
dep = "BSCS"
sec = ["A","B","C"]
faculty = {"A":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","Physics":"S4","FOCP":"S5","IoT":"S6","PKST":"S7","Calculus":"S8"},
           "B":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","Physics":"S4","FOCP":"S5","IoT":"S6","PKST":"S7","Calculus":"S8"},
           "C":{"Com Skills":"S1","Discrete":"S2","ICT":"S9","Physics":"S10","FOCP":"S11","IoT":"S12","PKST":"S7","Calculus":"S13"}}
subjects = [["Com Skills",0,2],["Discrete",0,3],["ICT",0,2],["Physics",0,3],["FOCP",0,3],["IoT",0,3],["PKST",0,2],["Calculus",0,3],["-",0,40-21]]
faculty = {}
faculty_table = {}

########### Consraints variable #################

days = len(header)                          #Number of days in timetable
T_slots = 8                                 #To store number of total slots
break_slot = 5                              #To store break slot
lecture_dur = 60                            #Lecture Duration
start_time = [9,00,00]                      #Starting time of first lecture
Timetable = []                              #List to store entire classes timetable

############ Create time slots ################

Time = []
timeobj= time(start_time[0],start_time[1],start_time[2])                    #Start from starting time
for x in range(T_slots):
    Time.append(str(timeobj)+"-"+str((datetime.combine(date.today(), timeobj) + timedelta(minutes=lecture_dur)).time()))
    timeobj = (datetime.combine(date.today(), timeobj) + timedelta(minutes=lecture_dur)).time()

########### Make initial timetable list #################

def emptytimetable():
    t = [[0 for x in range(days)] for x in range(T_slots-1)]
    t.insert(break_slot-1,["-" for x in range(days)])                       #Enter break in empty table
    return t

########## Take input from user ########

def take_input():
    global dep,T_slots,break_slot,lecture_dur,start_time,subjects,credit,sec,faculty
    print("*"*30)
    print("Timetable Generator prototype project made by Abdullah Saim")
    print("*"*30)
    print()
    print("Please enter all details properly:-")
    dep = input("Enter name of department: ")
    T_slots = int(input("Enter number of time slots: "))
    break_slot = int(input("Enter the break slot number: "))
    lecture_dur = int(input("Enter lecture duration: "))
    start_time = [int(x) for x in input("Enter start time: ").split(':')]
    sec = input("Enter name of sections seperated by comma: ").split(',')
    subjects_list = input("Enter subjects seperated by comma: ").split(',')
    credit = [int(x) for x in input("Enter repective credits seperated by comma: ").split(',')]
    subjects = [[subject,0,cr] for subject,cr in zip(subjects_list+["-"],credit+[T_slots*days-sum(credit)])]
    faculty = dict()
    for x in sec:
        temp = dict()
        for y in subjects_list:
            temp[y] = input("Enter name of teacher for "+y+" of section "+x+": ")
        faculty[x] = temp
        
take_input()                                                    #Call user input function

############### Check if the teacher has a lecture #############

def teacher(sub,row,col,sec):

    if row>1 and faculty_table[faculty[sec][sub]][row-1][col] != 0 and faculty_table[faculty[sec][sub]][row-2][col] != 0:
        return False
    if faculty_table[faculty[sec][sub]][row][col] != 0:         #Check if teacher has empty slot
        return False
    else:
        faculty_table[faculty[sec][sub]][row][col] = sec        #Assign the class to teacher
        return True
    
################# timetable generator function ###########

def generator(timetable,subj, row, col, sec):
   
    if (row == T_slots - 1 and col == days):                        #If in last row table is filled
        return True

    if col == days:                                                 #If in last column go to next row
        row += 1
        col = 0

    if timetable[row][col] != 0:                                    #If slot not empty go to next empty slot
        return generator(timetable,subj, row, col + 1, sec)
    for sub in subj:

        if sub[1] < sub[2]:                                         #Check if classes remaining
            if sub[0] != "-":
                if teacher(sub[0],row,col,sec):                     #Chwck if lecture assignable
                    sub[1] += 1
                    timetable[row][col] = sub[0]                    #Assign lecture to slot
                    if generator(timetable,subj, row, col + 1, sec):
                        return True
            else:
                    sub[1] += 1                                     #Increase number of assigned classes
                    timetable[row][col] = sub[0]
                    if generator(timetable,subj, row, col + 1, sec):
                        return True
        
        timetable[row][col] = 0
    return False

############## Generate first timetable ###############

def sgen(table):
    subs = deepcopy(subjects)                                   #Copy all subjects
    for sub in subs:
        if sub[0] == '-':
            continue
        while sub[1] < sub[2]:                                  #Check if class remaining
            while True:
                x = random.randint(0,T_slots-1)
                y = random.randint(0,days-1)
                if table[x][y] == 0:                            #Check if random selected slot assignable
                    table[x][y]=sub[0]
                    sub[1] += 1                                 #Assign subject
                    teacher(sub[0],x,y,"A")
                    break
    
    for x in range(len(table)):                                 #Assign all remaining slots as free
        for y in range(len(table[0])):
            if table[x][y] == 0:
                table[x][y] = "-"
    return table

##################### Create first Timetable #####################

for x in faculty.keys():                                        
    temp = dict()
    for y in faculty[x].keys():                                 #Initialize all teachers empty timetable
        faculty_table[faculty[x][y]] = emptytimetable()         
Timetable.append(sgen(emptytimetable()))                        #Create first timetable

##################### Create Timetable List #####################

for x in range(1,len(sec)):
    temp = deepcopy(subjects)
    Timetable.append(emptytimetable())                          #Start by asigning empty timetable to class
    if not generator(Timetable[x],temp, 0, 0,sec[x]):           #Call function to generate a suitable timetable
        print ("Could not create")                              
        quit()                                                  #IF not possible then quit

################### Display Class Time Table ##################

itr_sec = 0
for timetables in Timetable:
    print("-"*100)                                              #Display heading
    print ("|",(dep+" Timetable of Section "+sec[itr_sec]).center(97),"|")
    print("-"*100)
    print("Dates".center(20),end='|')
    for x in header:
        print(x.center(15),end='|')                             #Display days
    print()
    print("-"*100)                                              #Seperator line
    i = 0                                                       #Index Counter variable
    for x in timetables:
        print(Time[i].center(20),end='|')                       #Dsiplay timeslots
        i+=1
        for y in x:
            print(y.center(15),end='|')                         #Dsiplay Lectures
        print()
    print()
    itr_sec += 1                                                #Update section iterator
    
################## Display Faculty Time Table #####################

for timetables in faculty_table:
    print("-"*100)                                              #Heading of faculty timetable
    print ("|",(dep+" Timetable of "+timetables).center(97),"|")
    print("-"*100)
    print("Dates".center(20),end='|')
    for x in header:
        print(x.center(15),end='|')                             #Print days
    print()
    print("-"*100)
    i = 0
    for x in faculty_table[timetables]:                         #Get all faculty timetables
        print(Time[i].center(20),end='|')
        i+=1
        for y in x:                                             #Value 0 means free lecture
            print((str(y) if y != 0 and y != "-" else "Free").center(15),end='|')
        print()
    print()

############## Create class Timetable File #######################

itr_sec = 0
with open('Table.csv', 'w') as file:                            #Create csv file to write classes timetable
    writer = csv.writer(file)
    writer.writerow([])
    for table in Timetable:                                     #Enter heading
        writer.writerow(["","","",dep+ " Timetable of Section "+sec[itr_sec]])
        itr_sec += 1
        writer.writerow(["","Dates"]+header)                    #Enter dates
        for i in range(len(table)):
            writer.writerow(["",Time[i]]+table[i])              #Enter lectures
        writer.writerow([])
        
##############  Create Faculty Timetable File ##############

with open('Teachers.csv', 'w') as file:                         #Create csv fiie to write faculty timetable
    writer = csv.writer(file)
    writer.writerow([])
    for timetables in faculty_table:                            #Enter heading
        writer.writerow(["","",dep+" Timetable of "+timetables])
        writer.writerow(["","Dates"]+header)                    #Enter dates
        for i in range(len(faculty_table[timetables])):
            writer.writerow(["",Time[i]]+["Free" if x == 0 else x for x in faculty_table[timetables][i]])
        writer.writerow([])                                     #Enter assigned sections

############ Makeup lecture scheduling GUI function ############

def makeup_schedule(clas,makes):
    makeup = emptytimetable()                                   #empty table to track assignable slots
    for row in range(T_slots):
        for col in range(days):
            if Timetable[ord(clas)-65][row][col] == "-"  and faculty_table[faculty[clas][makes]][row][col] == 0 and row != break_slot-1:
                makeup[row][col] = 1                            #If assignable flag it
    root = Tk()
    root.title("Makeup Scheduler")
    root.geometry("1162x663")                                   #Window size
    label = Label(root, text = "Makeup Slots Available of "+makes+" for section "+clas, width=59, bg = "yellow", bd = 20, fg = "black", font = ('Castellar',17,'bold'))  
    label.grid(row=0, column=0, columnspan=6)                   #Heading
    label = Label(root, text = "Timeslots\\Days", bg = "green", bd = 20, width=20, fg = "white", font = ('Helvetica',16,'bold'))  
    label.grid(row=1, column=0)                           

    for h in range (len(header)):                               #Label days
        label = Label(root, text = header[h], bg = "red", bd = 20, width=10, fg = "white", font = ('Helvetica',16,'bold'))  
        label.grid(row=1, column=h+1)
        
    for t in range (len(Time)):                                 #Label time
        label = Label(root, text = Time[t], bg = "red", bd = 20, width=20, fg = "white", font = ('Helvetica',16,'bold'))  
        label.grid(row=t+2, column=0)

    for i in range(len(makeup)):                                #Break Slot
        if i == break_slot-1:
            e = Label(root, text="Break", bg='green', fg = 'white', bd = 20, width=63, font=('Arial',16,'bold'))
            e.grid(row=i+2, column=1, columnspan = 5)
            continue
        for j in range(len(makeup[0])):                         #Tick all assignable slots

            if makeup[i][j] == 1:
                e = Label(root, text="✓", bd = 13, width=7, fg='blue', font=('Arial',24,'bold'))
            else:
                e = Label(root, text="", bd = 20, width=10, font=('Arial',16,'bold'))
            
            e.grid(row=i+2, column=j+1)                         #Grid everything properly

    root.mainloop()
    
################# No selection Error handling ###################

def select(clas,makes):
    if clas == '' or makes == '':
        messagebox.showerror("Selection Error","Please select proper values")
    else:
        makeup_schedule(clas,makes)                             #If properly selected then call function
    
################### Prompting input for makup ##################

def askscheduler():
    
    root= Tk()                                                  #Create window for scheduler
    #Variables to store names
    selected_sub = StringVar()                                  #Variable to store subject name
    selected_sec = StringVar()                                  #Variable to store section name
    
    # config the root window
    root.geometry('300x200')
    root.resizable(False, False)                                #Make fixed size window
    root.title('Makeup Details')

    # label for subject
    label = Label(text="Please select a subject:")              #Create labels
    label.pack(fill=X, padx=5, pady=5)

    # create a combobox for subjects                            #Assign subject names to combobox
    sub_cb = ttk.Combobox(root,values=[sub[0] for sub in subjects][:-1], textvariable=selected_sub)
    sub_cb.current(0)
    # prevent typing a value
    sub_cb['state'] = 'readonly'                                #Make it readonly

    # place the widget
    sub_cb.pack(fill=X, padx=5, pady=5)                         #Place it on window

    # label for section
    label = Label(text="Please select a section:")              #Lebel for section
    label.pack(fill=X, padx=5, pady=5)                          

    # create a combobox                                         #Give list of sections to section combobox
    sec_cb = ttk.Combobox(root,values = sec, textvariable=selected_sec)
    sec_cb.current(0)
    # prevent typing a value
    sec_cb['state'] = 'readonly'                                #Make it readonly

    # place the widget
    sec_cb.pack(fill=X, padx=5, pady=5)                         #Place it

    Button(root, text= "Find", command=lambda: select(selected_sec.get(),selected_sub.get())).pack(fill=X, padx=5, pady=5)
                                                                #Create button to askscheduler
    root.mainloop()

############# Ask for confirmation ####################

if messagebox.askyesno(title='Scheduler', message='Do you want to schedule a makeup class?'): askscheduler()
messagebox.showinfo('Thank You','This Scheduling system is made by Saim')

######################### END ##########################
