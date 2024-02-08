from time import strftime
from tkinter import Label, Tk
from uiColors import *


#Labels
clockLabel = uiClockLabel
dateLabel = uiDateLabel
clockLabel.place(x = 10, y = 20)
dateLabel.place(x = 10, y = 90)

def updateLabel():
    currentTime = strftime('%H:%M:%S')     #Getting current hour, minutes and seconds
    dateToday = strftime("%A, %d %B %Y")      #Getting current day, date and month
    clockLabel.config(text = currentTime)        #Setting text to show current time
    dateLabel.config(text = dateToday)          #Setting text to show current date
    window.after(1000, updateLabel)           #Updating every second (1000 milliseconds)

updateLabel()
window.mainloop()
