
import tkinter as tk
#import tk
import subprocess, csv, os
import webbrowser

window = tk.Tk()
window.geometry("800x400")
window.configure(bg="#910ba0")

parent_path = ((os.path.dirname(os.path.realpath(__file__))).replace("\\","/"))
if parent_path[-1] == "/":
    parent_path = parent_path[0:-1]

#widgets
textBox=tk.Entry(window,width=80)
textBox.grid(column=2,row=10,pady=(100,5))
textBox.insert(0, parent_path)


options = ["June","November"]

clicked = tk.StringVar()
MONTH = tk.StringVar()
PAPER = tk.StringVar()
YEAR = tk.StringVar()
# initial menu text
MONTH.set("June")
PAPER.set("12")
YEAR.set(2010)

def go(MONTH,PAPER,YEAR):
    text = ""
    month = MONTH.get()
    papers = PAPER.get()
    year = YEAR.get()

    if month == "November":
        if int(year) > 2017:
            month = "oct-nov"
            season = "w"
        else:
            month = "nov"
            season = "w"
    elif month == "June":
        if int(year) > 2017:
            month = "may-june"
            season = "s"
        else:
            month = "jun"
            season = "s"

        if int(year) == 2020:
            text = (f"https://pastpapers.papacambridge.com/viewer/caie/cambridge-advanced-as-and-a-level-physics-9702-{month}-{year}-9702-{season}{year[2::]}-ms-{papers}-pdf")

    if text == "":
        text = (f"https://pastpapers.papacambridge.com/viewer/caie/cambridge-advanced-as-and-a-level-physics-9702-{year}-{month}-9702-{season}{year[2::]}-ms-{papers}-pdf")

    textBox.delete(0, "end")
    textBox.insert(0,text)
    webbrowser.open(text)

# Create Dropdown menu
drop = tk.OptionMenu(window, MONTH, *["June","November"])
drop.grid(column = 1, row=1, pady=(20,20))

drop = tk.OptionMenu(window, PAPER, *["12","22","11","21"])
drop.grid(column = 2, row=1, pady=(20,20))

drop = tk.OptionMenu(window, YEAR, *[str(x) for x in range(2010,2022)])
drop.grid(column = 3, row=1, pady=(20,20))

refresh_button=tk.Button(window, height=2, width=20, text="Refresh",command=lambda: go(MONTH,PAPER,YEAR))
refresh_button.grid(column=2,row=2)

window.mainloop()
