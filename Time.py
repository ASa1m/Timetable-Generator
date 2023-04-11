import random
import datetime
from datetime import datetime, date, time, timedelta

header = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

Time = []
timeobj= time(9,00,00)
for x in range(8):
    Time.append(str(timeobj)+"-"+str((datetime.combine(date.today(), timeobj) + timedelta(minutes=60)).time()))
    timeobj = (datetime.combine(date.today(), timeobj) + timedelta(minutes=60)).time()

def emptytimetable():
    return [[0 for x in range(5)] for x in range(7)]

Timetable = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]

def gen(timetable):
    subs = [["Com",0,2],["Dis",0,3],["ICT",0,2],["ICT Lab",0,3],["FOCP",0,3],["FOCP Lab",0,3],["PKST",0,2],["Cal",0,3],["-",0,100]]
    for x in range(7):
        for y in range(5):
            while True:
                s = random.randint(0,8)
                if subs[s][1] < subs[s][2]:
                    timetable[x][y] = subs[s][0]
                    subs[s][1] += 1
                    break
                
    timetable.insert(4,["-","-","-","-","-"])
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

        #temp.insert(4,["-","-","-","-","-"])

    
Timetable[0] = gen(emptytimetable())
for x in range(2):
    Table_add()



for timetables in Timetable:
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
