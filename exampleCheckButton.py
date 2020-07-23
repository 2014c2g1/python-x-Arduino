import tkinter
import pyfirmata
from time import sleep

def onStartButtonPress():
    redPin.write(redVar.get())
    greenPin.write(greenVar.get())
def onStopButtonPress():
    redPin.write(0)
    greenPin.write(0)
port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
#指定數位腳位11,10為數位輸出模式
redPin = board.get_pin('d:11:o')
greenPin = board.get_pin('d:10:o')


top = tkinter.Tk()
top.title("exampleCheckButton")
top.minsize(300,75)

redVar = tkinter.IntVar()
redCheckBox = tkinter.Checkbutton(top,text="Red LED",variable=redVar)
redCheckBox.grid(column=1, row=1)

greenVar = tkinter.IntVar()
greenCheckBox = tkinter.Checkbutton(top,text="Green LED",variable=greenVar)
greenCheckBox.grid(column=2, row=1)

startButton = tkinter.Button(top,text="Start",command= onStartButtonPress)
#startButton.pack()
startButton.grid(column=1, row=2)

stopButton = tkinter.Button(top,text="Stop",command=onStopButtonPress)
stopButton.grid(column=2, row=2)

exitButton = tkinter.Button(top,text="Exit",command=top.quit)
exitButton.grid(column=3, row=2)

top.mainloop()
