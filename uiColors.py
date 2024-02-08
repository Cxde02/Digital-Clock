import tkinter

#Window configuration for clock
window = tkinter.Tk()
window.title("Digital Clock")
window.geometry('450x170')  #Width x Height
window.configure(bg='#092635')   #Background color of window
window.resizable(False, False)    #Prevents user from resizing the window

uiClockLabel = tkinter.Label(window, font=('Courier New', 50), bg="#092635", fg="#DAFFFB")
uiDateLabel = tkinter.Label(window, font=('Barlow', 20,  'bold'), bg="#092635", fg="#16FF00")