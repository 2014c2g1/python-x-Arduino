import tkinter
import pyfirmata
from time import sleep

def onStartButtonPress():
	#延遲參數是來自Entry小工具的輸入
	timePeriod = timePeriodEntry.get()
	timePeriod = float(timePeriod)
	startButton.config(state=tkinter.DISABLED)
	ledPin.write(1)
	sleep(timePeriod)
	ledPin.write(0)
	startButton.config(state=tkinter.ACTIVE)


port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:11:o')



top = tkinter.Tk()
top.title("Specify time using Entry")
top.minsize(300,30)
timePeriodEntry =tkinter.Entry(top,bd=5,width=25)
timePeriodEntry.pack()
timePeriodEntry.focus_set()

startButton = tkinter.Button(top,text="Start",command= onStartButtonPress)
startButton.pack()


top.mainloop()
