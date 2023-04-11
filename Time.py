import random
from tkinter import *
import datetime
from copy import deepcopy
import csv
from datetime import datetime, date, time, timedelta

############################

header = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
dep = "BSCS"
sec = ["A","B","C","D","E"]
faculty = {"A":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "B":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "D":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "E":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "B":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},

           "C":{"Com Skills":"S1","Discrete":"S2","ICT":"S9","ICT Lab":"S10","FOCP":"S11","FOCP Lab":"S12","PKST":"S7","Calculus":"S13"}}
subjects = [["Com Skills",0,2],["Discrete",0,3],["ICT",0,2],["ICT Lab",0,3],["FOCP",0,3],["FOCP Lab",0,3],["PKST",0,2],["Calculus",0,3],["-",0,40-21]]

faculty_table = {}
############################

days = len(header)
T_slots = 8
break_slot = 5
lecture_dur = 60
start_time = [9,00,00]
Timetable = []

############################

Time = []
timeobj= time(start_time[0],start_time[1],start_time[2])
for x in range(T_slots):
    Time.append(str(timeobj)+"-"+str((datetime.combine(date.today(), timeobj) + timedelta(minutes=lecture_dur)).time()))
    timeobj = (datetime.combine(date.today(), timeobj) + timedelta(minutes=lecture_dur)).time()

############################

def emptytimetable():
    return [[0 for x in range(days)] for x in range(T_slots-1)]

############################

def generator(timetable,subj, row, col, sec):
   
    if (row == T_slots - 1 and col == days):
        return True

    if col == days:
        row += 1
        col = 0

    if timetable[row][col] != 0:
        return generator(timetable,subj, row, col + 1, sec)
    for sub in subj:

        #if sub[1] < sub[2] and new_conflict(sub[0],row,col,sec):
        if sub[1] < sub[2]:
            if sub[0] != "-":
                if teacher(sub[0],row,col,sec):
                    timetable[row][col] = sub[0]
                    sub[1] += 1
                    if generator(timetable,subj, row, col + 1, sec):
                        return True
            else:
                    timetable[row][col] = sub[0]
                    sub[1] += 1
                    if generator(timetable,subj, row, col + 1, sec):
                        return True

 
        timetable[row][col] = 0
    return False

############################

def teacher(sub,row,col,sec):
    if len(faculty_table) == 0: faculty_table.update({faculty[sec][sub] : emptytimetable()})
    
    if faculty[sec][sub] in faculty_table:
        if row>1 and faculty_table[faculty[sec][sub]][row-2][col] != 0 and faculty_table[faculty[sec][sub]][row-1][col] != 0:
            #print ("Did at ", faculty_table[faculty[sec][sub]])
            return False
        if faculty_table[faculty[sec][sub]][row][col] != 0:
            return False
        else:
            faculty_table[faculty[sec][sub]][row][col] = sec
            return True
    else:
        faculty_table[faculty[sec][sub]] = emptytimetable()
        teacher(sub,row,col,sec)
    
    
############################

def new_conflict(val,x,y,sec):
    for table in Timetable:
        if val == table[x][y] and val != "-":
            return False
    return True

#############################

# def sgen(table):
#     subs = deepcopy(subjects)
#     table.insert(break_slot-1,["-" for x in range(days)])
#     for sub in subs:
#         while sub[1] < sub[2]:
#             while True:
#                 x = random.randint(0,T_slots-1)
#                 y = random.randint(0,days-1)
#                 if table[x][y] == 0:
#                     table[x][y]=sub[0]
#                     sub[1] += 1   
#                     if faculty["A"][sub[0]] not in faculty_table:
#                         faculty_table.update({faculty["A"][sub[0]] : emptytimetable()})
#                         faculty_table[faculty["A"][sub[0]]].insert(break_slot-1,[0 for x in range(days)])

#                     else:
#                         faculty_table[faculty["A"][sub[0]]][x][y] = "A"
#                 break
    
#     for x in range(len(table)):
#         for y in range(len(table[0])):
#             if table[x][y] == 0:
#                 table[x][y] = "-"
#     return table

            
    
#     while True:
#         for x in range(T_slots-2,-1,-1):
#             for y in range(days):
#                 while True:
#                     s = random.randint(0,len(subs)-1)
#                     if subs[s][0] != "-":
#                         faculty_table.update({faculty["A"][subs[s][0]] : emptytimetable()})

#                     if timetable[x][y] != 0: break
                    
#                     if "Lab" in subs[s][0] and subs[s][1] < subs[s][2]:
#                         if x==1 or x==4:
#                             timetable[x][y] = timetable[x+1][y] = timetable[x+2][y] = subs[s][0]
#                             subs[s][1] = 3
#                             break
#                     elif "Lab" not in subs[s][0] and subs[s][1] < subs[s][2]:
#                         timetable[x][y] = subs[s][0]
#                         subs[s][1] += 1
#                         if subs[s][0] != "-":
#                             faculty_table[faculty["A"][subs[s][0]]][x][y] = sec

#                         break

#         sum = 0
#         for i in range(len(subs)-1):
#             sum += subs[i][1]
#         if sum == 21:
#             return timetable
        
# ############################

# def conflict(table,temp):
#     for x in range(len(table)):
#         for y in range(len(table[0])):
#             if temp[x][y] == table[x][y] and temp[x][y] != "-":
#                 return True
#     return False

# ############################

# def Table_add():
#     global Timetable
#     if len(Timetable) == 0 :
#         Timetable.append(gen(emptytimetable()))
#         return
#     while True:
#         temp = gen(emptytimetable())

#         for table in Timetable:
#             if conflict(table,temp):
#                 break
#         else:
#             Timetable.append(temp)
#             return    

##################### Create Timetable List #####################

#Timetable.append(sgen(emptytimetable()))

for x in range(len(sec)):
    temp = deepcopy(subjects)
    Timetable.append(emptytimetable())
    Timetable[x].insert(break_slot-1,["-" for x in range(days)])
    if not generator(Timetable[x],temp, 0, 0,sec[x]):
        print ("Could not create")
        quit()

################### Display Class Time Table ##################

itr_sec = 0
for timetables in Timetable:
    print("-"*100)
    print ("|",(dep+" Timetable of Section "+sec[itr_sec]).center(97),"|")
    print("-"*100)
    print("Dates".center(20),end='|')
    for x in header:
        print(x.center(15),end='|')
    print()
    print("-"*100)
    i = 0
    for x in timetables:
        print(Time[i].center(20),end='|')
        i+=1
        for y in x:
            print(y.center(15),end='|')
        print()
    print()
    itr_sec += 1
    
################## Display Faculty Time Table #####################

for timetables in faculty_table:
    print("-"*100)
    print ("|",(dep+" Timetable of "+timetables).center(97),"|")
    print("-"*100)
    print("Dates".center(20),end='|')
    for x in header:
        print(x.center(15),end='|')
    print()
    print("-"*100)
    i = 0
    faculty_table[timetables].insert(break_slot-1,["-" for x in range(days)])
    for x in faculty_table[timetables]:
        print(Time[i].center(20),end='|')
        i+=1
        for y in x:
            print((str(y) if y != 0 and y != "-" else "Free").center(15),end='|')
        print()
    print()

############## Create Timetable File #######################
itr_sec = 0
with open('Table.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([])
    for table in Timetable:
        writer.writerow(["","","",dep+ " Timetable of Section "+sec[itr_sec]])
        itr_sec += 1
        writer.writerow(["","Dates"]+header)
        for i in range(len(table)):
            writer.writerow(["",Time[i]]+table[i])
        writer.writerow([])
        
##############  Create Faculty Timetable File ##############
with open('Teachers.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([])
    for timetables in faculty_table:
        writer.writerow(["","","",dep+" Timetable of "+timetables])
        writer.writerow(["","Dates"]+header)
        for i in range(len(faculty_table[timetables])):
            writer.writerow(["",Time[i]]+["Free" if x == 0 else x for x in faculty_table[timetables][i]])
        writer.writerow([])

########################################################
clas = "C"
makes = "ICT"
makeup = emptytimetable()
makeup.insert(break_slot-1,["-" for x in range(days)])
for row in range(T_slots):
    for col in range(days):
        if Timetable[ord(clas)-65][row][col] == "-"  and faculty_table[faculty[clas][makes]][row][col] == 0 and row != break_slot-1:
            makeup[row][col] = 1
            
########################################################################
root = Tk()
root.title("Makeup Scheduler")
		# code for creating table
  
label = Label(root, text = "Makeup Slots Available of "+makes+" for section "+clas, width=59, bg = "yellow", bd = 20, fg = "black", font = ('Castellar',17,'bold'))  
label.grid(row=0, column=0, columnspan=6)
label = Label(root, text = "Timeslots\\Days", bg = "green", bd = 20, width=20, fg = "white", font = ('Helvetica',16,'bold'))  
label.grid(row=1, column=0)

for h in range (len(header)):
    label = Label(root, text = header[h], bg = "red", bd = 20, width=10, fg = "white", font = ('Helvetica',16,'bold'))  
    label.grid(row=1, column=h+1)
    
for t in range (len(Time)):
    label = Label(root, text = Time[t], bg = "red", bd = 20, width=20, fg = "white", font = ('Helvetica',16,'bold'))  
    label.grid(row=t+2, column=0)

for i in range(len(makeup)):
    if i == break_slot-1:
        e = Label(root, text="Break", bg='green', fg = 'white', bd = 20, width=63, font=('Arial',16,'bold'))
        e.grid(row=i+2, column=1, columnspan = 5)
        continue
    for j in range(len(makeup[0])):

        if makeup[i][j] == 1:
            e = Label(root, text="✓", bd = 13, width=7, fg='blue', font=('Arial',24,'bold'))
        else:
            e = Label(root, text="", bd = 20, width=10, font=('Arial',16,'bold'))
        
        e.grid(row=i+2, column=j+1)

root.mainloop()

#################################################
