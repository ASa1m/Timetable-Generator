import random
import datetime
from datetime import datetime, date, time, timedelta

header = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
dep = "BSCS"
sec = ["A","B","C","D","E","F"]
faculty = {"A":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "B":{"Com Skills":"S1","Discrete":"S2","ICT":"S3","ICT Lab":"S4","FOCP":"S5","FOCP Lab":"S6","PKST":"S7","Calculus":"S8"},
           "C":{"Com Skills":"S1","Discrete":"S2","ICT":"S9","ICT Lab":"S10","FOCP":"S11","FOCP Lab":"S12","PKST":"S7","Calculus":"S13"}}
subjects = (["Com Skills",0,2],["Discrete",0,3],["ICT",0,2],["ICT Lab",0,3],["FOCP",0,3],["FOCP Lab",0,3],["PKST",0,2],["Calculus",0,3],["-",0,50])

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

def generator(timetable,subj, row, col):
   
    if (row == T_slots - 1 and col == days):
        return True
       

    if col == days:
        row += 1
        col = 0
 

    if timetable[row][col] != 0:
        return generator(timetable,subj, row, col + 1)
    for sub in subj:

        if sub[1] < sub[2] and new_conflict(sub[0],row,col):

                
            timetable[row][col] = sub[0]
            sub[1] += 1

            if generator(timetable,subj, row, col + 1):
                return True
 

        timetable[row][col] = 0
    return False
############################
def new_conflict(val,x,y):
    for table in Timetable:
        if val == table[x][y] and val != "-":
            return False
    return True

####################################################################################################

def gen(timetable):
    
    while True:
        subs = subjects
        for x in range(T_slots-2,-1,-1):
            for y in range(days):
                while True:
                    s = random.randint(0,len(subs)-1)
                    if timetable[x][y] != 0: break
                    if "Lab" in subs[s][0] and subs[s][1] < subs[s][2]:
                        if x==1 or x==4:
                            timetable[x][y] = timetable[x+1][y] = timetable[x+2][y] = subs[s][0]
                            subs[s][1] = 3
                            break
                    elif "Lab" not in subs[s][0] and subs[s][1] < subs[s][2]:
                        timetable[x][y] = subs[s][0]
                        subs[s][1] += 1
                        break

                    
                    
        timetable.insert(break_slot-1,["-" for x in range(days)])
        sum = 0
        for i in range(len(subs)-1):
            sum += subs[i][1]
        if sum == 21:
            return timetable
        

#######################################
def conflict(table,temp):
    for x in range(len(table)):
        for y in range(len(table[0])):
            if temp[x][y] == table[x][y] and temp[x][y] != "-":
                return True
    return False
#######################################
def Table_add():
    global Timetable
    if len(Timetable) == 0 :
        Timetable.append(gen(emptytimetable()))
        return
    while True:
        temp = gen(emptytimetable())

        for table in Timetable:
            if conflict(table,temp):
                break
        else:
            Timetable.append(temp)
            return    

##########################################
    
for x in range(len(sec)):
    temp = [["Com Skills",0,2],["Discrete",0,3],["ICT",0,2],["ICT Lab",0,3],["FOCP",0,3],["FOCP Lab",0,3],["PKST",0,2],["Calculus",0,3],["-",0,50]]
    #Table_add()
    Timetable.append(emptytimetable())
    Timetable[x].insert(break_slot-1,["-" for x in range(days)])

    generator(Timetable[x],temp, 0, 0)


################################
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
