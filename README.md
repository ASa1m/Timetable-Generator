
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
Outputs timetables to CSV files ("*Table.csv*" and "*Teachers.csv*").
### Makeup Schedule GUI:

Provides an intuitive graphical interface for makeup class scheduling.
Highlights available slots for makeup classes, simplifying the rescheduling process.
### Error Handling:

Incorporates error handling mechanisms to ensure proper input selection.
### User Interaction:

Prompts users with a confirmation dialog to schedule makeup classes.
## How to Use
### Requirements:

Ensure you have Python installed.
Install Tkinter if not already using `pip install tk`.
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

### Automation
User imput can be automated using the `Automate.py` script which uses `pyautogui` to input text
## Acknowledgements
This project was developed by [ASa1m](https://github.com/ASa1m). Feel free to contribute or provide feedback. Enjoy efficient class scheduling!
