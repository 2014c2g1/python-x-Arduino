import sys, csv
import matplotlib.pyplot as plt
import pyfirmata
from time import sleep
import numpy as np
import time
import tkinter

port = 'com3'
board = pyfirmata.Arduino(port)

#即時繪圖迴圈
def onStartButtonPress():
    while True:
        if flag.get():
            sleep(1)
            pData.append(float(a0.read()))
            plt.ylim([0, 1])
            del pData[0]
            l1.set_xdata(x)
            l1.set_ydata(pData)  # update the data
            plt.draw()  # update the plot
            top.update()
        else:
            flag.set(True)
            break


def onPauseButtonPress():
    flag.set(False)


def onExitButtonPress():
	print ("Exiting....")
	onPauseButtonPress()
	board.exit()
	pyplot.close(fig)
	top.quit()
	top.destroy()
	print ("Done.")
	sys.exit()
top = tkinter.Tk()
top.title("Tkinter + matplotilb")
top.minsize(300,30)
flag = tkinter.BooleanVar(top)
flag.set(True)


#使用遞回執行緒來避免軟衝區溢位
it = pyfirmata.util.Iterator(board)
it.start()

#指定類比腳位A0的角色與變數
a0 = board.get_pin('a:0:i')
x = np.linspace(0, 25, 25)

#初始化互動模式
plt.ion()
pData = [0] * 25
figure, ax = plt.subplots(figsize=(8,6))
plt.title('Real-time Potentiometer reading')
#ax1 = plt.axes()
l1, = ax.plot(x,pData)
plt.ylim([0,1])
plt.xlim([0,25])


startButton = tkinter.Button(top,text = "Start",command = onStartButtonPress)
startButton.grid(column = 1,row = 2)


pauseButton = tkinter.Button(top,text = "Pause",command = onPauseButtonPress)
pauseButton.grid(column = 2,row = 2)

exitButton = tkinter.Button(top,text = "Exit",command = onExitButtonPress)
exitButton.grid(column = 3,row = 2)



top.mainloop()