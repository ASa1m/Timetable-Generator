
# Time Table Generator Project (Python)
This Python-based Time Table Generator project automates the scheduling of classes for a computer science department. The project features a graphical user interface (GUI) developed using Tkinter and includes randomization and scheduling constraints.

## Key Features
### User Input:

Department name, time slots, break slot, lecture duration, start time, sections, subjects, and credits.
Timetable Generation:

Utilizes a backtracking algorithm to create clash-free schedules.
Randomly generates the first timetable and refines it for each section.
### Output Display:

Displays class and faculty timetables with detailed information.
![image](https://github.com/ASa1m/Timetable-Generator/assets/94314354/6a788217-2bbe-4b1e-a9df-4460f26c7aec)

Outputs timetables to CSV files ("*Table.csv*" and "*Teachers.csv*").
![image](https://github.com/ASa1m/Timetable-Generator/assets/94314354/1d476b7e-5b24-4cf2-8fdb-c5efce59d45e)

### Makeup Schedule GUI:

Provides an intuitive graphical interface for makeup class scheduling.
Highlights available slots for makeup classes, simplifying the rescheduling process.
![image](https://github.com/ASa1m/Timetable-Generator/assets/94314354/cf8ac7d4-b2b8-4d21-9081-78a8f4d30d13)

### Error Handling:

Incorporates error handling mechanisms to ensure proper input selection.

### User Interaction:

Prompts users with a confirmation dialog to schedule makeup classes.
![image](https://github.com/ASa1m/Timetable-Generator/assets/94314354/d479a5e7-6213-4d3a-a682-78ebdd1fbb5e)

## How to Use
### Requirements:

Ensure you have Python installed.
<br>Install Tkinter if not already using `pip install tk`.
<br>Install pyautogui for Automation (optional) `pip install pyautogui`.

### Run the Program:

Execute the program using `python Time.py`.
Follow the prompts to input department details and preferences.
### View Timetables:

Timetables will be displayed on the console.
Class and faculty timetables are also saved as CSV files.

### Makeup Scheduling:

If prompted, use the GUI to schedule makeup classes efficiently.
Files
timetable_generator.py: The main Python script for the Time Table Generator.
Table.csv: CSV file containing class timetables.
Teachers.csv: CSV file containing faculty timetables.
![image](https://github.com/ASa1m/Timetable-Generator/assets/94314354/72385e8b-ddf2-4e12-bd34-e15ff1721ec6)

### Automation
User imput can be automated using the `Automate.py` script which uses `pyautogui` to input text

## Acknowledgements
This project was developed by [ASa1m](https://github.com/ASa1m). Feel free to contribute or provide feedback. Enjoy efficient class scheduling!
