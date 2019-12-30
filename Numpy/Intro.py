import numpy
# NumPy is the fundamental package for scientific computing in Python. It is a Python library that
# provides a multidimensional array object, various derived objects (such as masked arrays and matrices),
# and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting,
# selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

n = numpy.arange(27)    # creates a 1-d array
print(n,"\n")

print(n.reshape(3,9), "\n")   # This prints a 2-d array out of the given array
print(n.reshape(3,3,3), "\n") # printing the 3-d array
