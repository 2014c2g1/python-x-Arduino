import sys, csv
import matplotlib.pyplot as plt
import pyfirmata
from time import sleep
import numpy as np
import time

port = 'com3'
board = pyfirmata.Arduino(port)

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

#即時繪圖迴圈
while True:
	try:

		sleep(1)
		pData.append(float(a0.read()))
		plt.xlim([0,25])
		plt.ylim([0,1])
		del pData[0]
		l1.set_xdata(x)
		l1.set_ydata(pData) #更新資料
		#plt.draw() #更新圖表
		figure.canvas.draw()
		figure.canvas.flush_events()

	except KeyboardInterrupt:
		board.exit()
		break