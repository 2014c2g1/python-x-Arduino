import tkinter
import pyfirmata
from time import sleep

def onStartButtonPress():
    #延遲參數是來自Entry小工具的輸入
    timePeriod = timePeriodEntry.get()
    timePeriod = float(timePeriod)
    #亮度參數是來自Scale小工具的輸入
    ledBrightness = brightnessScale.get()
    ledBrightness = float(ledBrightness)
    startButton.config(state=tkinter.DISABLED)
    ledPin.write(ledBrightness/100.0)
    sleep(timePeriod)
    ledPin.write(0)
    startButton.config(state=tkinter.ACTIVE)


port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
#指定數位腳位11為PWM模式
ledPin = board.get_pin('d:11:p')



top = tkinter.Tk()
top.title("Specify time using Scale")
top.minsize(300,50)
timePeriodEntry =tkinter.Entry(top,bd=5,width=25)
timePeriodEntry.pack()
timePeriodEntry.focus_set()

brightnessScale = tkinter.Scale(top,from_=0,to=100,orient=tkinter.HORIZONTAL)
brightnessScale.pack()

startButton = tkinter.Button(top,text="Start",command= onStartButtonPress)
startButton.pack()


top.mainloop()
