# Stacking arrays
import cv2
import numpy

im_g = cv2.imread("smallgray.png", 0)

im_h = numpy.hstack((im_g, im_g))  # horizontal stack
print(im_h, "\n")

im_v = numpy.vstack((im_g, im_g)) # vertical stack
print(im_v, "\n")

# Note: Only arrays with similar dimensions can be stacked.

# Splitting :
lst = numpy.hsplit(im_v,5)
print(lst, "\n")

mst = numpy.vsplit(im_v, 3)
print(mst)
