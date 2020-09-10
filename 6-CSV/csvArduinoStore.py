import csv
import pyfirmata
from time import sleep
port ='com3'
board = pyfirmata.Arduino(port)

it  = pyfirmata.util.Iterator(board)
it.start()

pirPin = board.get_pin('d:11:i')
a0 = board.get_pin('a:0:i')

with open ('SensorDataStore.csv','w',newline = '') as f:
	w = csv.writer(f)
	w.writerow(["Number","Potentiometer","Motion sensor"])
	i = 0
	sleep(1)
	pirData = pirPin.read()
	potData = a0.read()
	print("begin")
	while i < 25:
		sleep(1)
		pirData = pirPin.read()
		potData = a0.read()
		if potData is not None:
			i += 1
			row = [i ,potData,pirData]
			w.writerow(row)
			print(i)
			print(potData)
			print(pirData)
		else:
			print("sonor is alarm")
			i += 1
			row = [i ,potData,pirData]
			w.writerow(row)
			print(i)
			print(potData)
			print(pirData)
print("Done. CSV file is ready")
sleep(3)
board.exit()