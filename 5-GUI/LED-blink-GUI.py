import tkinter
import pyfirmata
from time import sleep

port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin=board.get_pin('d:11:o')

def onStartButtonPress():
	startButton.config(state=tkinter.DISABLED)
	ledPin.write(1)
	sleep(1)
	ledPin.write(0)
	sleep(1)
	ledPin.write(1)
	sleep(1)
	ledPin.write(0)
	startButton.config(state=tkinter.ACTIVE)

#初始化主視窗，包括其標題與尺寸
top = tkinter.Tk()
top.title("Blink LED using button")
top.minsize(300,30)

startButton = tkinter.Button(top,text ="Start",command=onStartButtonPress)
startButton.pack()

top.mainloop()
