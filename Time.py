import random
import datetime
from datetime import datetime, date, time, timedelta

header = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
dep = "BSCS"
sec = ["A","B","C"]

############################
days = 5
T_slots = 8
break_slot = 5
lecture_dur = 60
start_time = [9,00,00]
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

#Timetable = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]
Timetable = [[]]

def gen(timetable):
    
    while True:
        subs = [["Com",0,2],["Dis",0,3],["ICT",0,2],["ICT Lab",0,3],["FOCP",0,3],["FOCP Lab",0,3],["PKST",0,2],["Cal",0,3],["-",0,50]]
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
        


def conflict(table,temp):
    for x in range(len(table)):
        for y in range(len(table[0])):
            if temp[x][y] == table[x][y] and temp[x][y] != "-":
                return False
    return True

def Table_add():
    global Timetable
    while True:
        temp = gen(emptytimetable())

        for table in Timetable:
            if conflict(table,temp):
                Timetable.append(temp)
                return    

Timetable[0] = gen(emptytimetable())

    
for x in range(2):
    
    Table_add()


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
