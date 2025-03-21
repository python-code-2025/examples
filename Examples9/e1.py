import numpy
arr = numpy.arange(10, 55, 5)
print(arr)
print(arr[:3])

second_array=numpy.array([1,3,9])
print(second_array)

third_array=numpy.array([
    [1,2,3],
    [11,12,13],
    [21,22,23]
])

print(third_array)
#print elemen of row=2, col=1
print(third_array[1][0])

#calculate 2 power 3
print(f"2 power 3 = {numpy.power(2,3)}")
