import numpy as np

arr = np.random.randint(1, 100, (2,3))
print(arr)
print("First Row and type of the array")
print(arr[1, :], arr.dtype)

weights=np.array([56.7, 12.44, 5.9])
print(weights.dtype)