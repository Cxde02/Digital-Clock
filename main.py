from time import strftime
from tkinter import Label, Tk

#Window configuration for clock
window = Tk()
window.title("Digital Clock")
window.geometry('450x150')  #Width x Height
window.configure(bg='#092635')   #Background color of window
window.resizable(False, False)    #Prevents user from resizing the window

#Labels
clockLabel = Label(window, font=('Courier New', 50, 'bold'), bg="#092635", fg="#DAFFFB")
dateLabel = Label(window, font=('Barlow', 20,  'bold'), bg="#092635", fg="#16FF00")
clockLabel.place(x= 20, y = 20)
dateLabel.place(x= 20, y = 100)

def updateLabel():
    currentTime = strftime( '%H:%M:%S')     #Getting current hour, minutes and seconds
    dateToday = strftime("%A, %d %B %Y")      #Getting current day, date and month
    clockLabel.config(text=currentTime)        #Setting text to show current time
    dateLabel.config(text=dateToday)          #Setting text to show current date
    window.after(1000, updateLabel)           #Updating every second (1000 milliseconds)

updateLabel()
window.mainloop()