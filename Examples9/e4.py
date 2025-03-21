import numpy as np
arr = np.random.randint(1, 100, (3,3))
np.savetxt("data.csv", arr, delimiter=",")
loaded_arr = np.loadtxt("data.csv", delimiter=",")
print(loaded_arr)