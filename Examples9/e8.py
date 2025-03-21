import numpy as np
import matplotlib.pyplot as pyplot 
x,y = np.loadtxt("example.csv", unpack=True, delimiter=',')

#pyplot.scatter(x,y, label="Length of fish based on age")
pyplot.plot(x,y,"bo-", label="Length of fish based on age")
pyplot.xlabel("Age / month")
pyplot.ylabel("Length / cm")
pyplot.legend()
pyplot.grid()
pyplot.show()