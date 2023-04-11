import pyautogui

pyautogui.sleep(5)

sec = ["A","B","C"]
subjects = ["Com Skills","Discrete","ICT","Physics","FOCP","IoT","PKST","Calculus"]
faculty = ["Sir Usman","Ma'am Saira","S3","S4","S5","S6","Ma'am Sobia","S8","Sir Usman","Ma'am Saira","S3","S4","S5","S6","Ma'am Sobia","S8","Sir Usman","Ma'am Saira","Sir Arsalan","Sir Hassan","Sir Jaudat","Sir Daniyal","Ma'am Sobia","Sir Ibrar"]
cr = [str(x) for x in [2,3,2,3,3,3,2,3]]

ins = [
    "BSCS",
    "8",
    "5",
    "60",
    "9:00:00",
    ",".join(sec),
    ",".join(subjects),
    ",".join(cr),
    ]

for x in ins:
    pyautogui.write(x)
    pyautogui.press('enter')

for x in faculty:
    pyautogui.write(x)
    pyautogui.press('enter')

