from matplotlib import pyplot
import random

x = range(0,25)
y = [random.randint(0,100) for r in range(0,25)]

figi = pyplot.figure()

pyplot.plot(x,y,'-')
pyplot.title('First Plot - Random integers')
pyplot.xlabel('X Axis')
pyplot.ylabel('Y Axis')

pyplot.show()