import sys, csv
from matplotlib import pyplot
import pyfirmata
from time import sleep
import numpy as np

port = 'com3'
board = pyfirmata.Arduino(port)

#使用遞回執行緒來避免軟衝區溢位
it = pyfirmata.util.Iterator(board)
it.start()

#指定類比腳位A0的角色與變數
a0 = board.get_pin('a:0:i')
x = np.linspace(0, 25, 25)
#初始化互動模式
pyplot.ion()
pData = [0] * 25
fig = pyplot.figure()
pyplot.title('Real-time Potentiometer reading')
#ax1 = pyplot.axes()
l1, = pyplot.plot(x,pData)
pyplot.ylim([0,1])

#即時繪圖迴圈
while True:
	try:
		sleep(1)
		pData.append(float(a0.read()))
		pyplot.ylim([0,1])
		del pData[0]
		l1.set_xdata([i for i in range(25) ])
		l1.set_ydata(pData) #更新資料
		pyplot.draw() #更新圖表
	except KeyboardInterrupt:
		board.exit()
		break