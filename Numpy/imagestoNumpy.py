import cv2

im_g = cv2.imread("smallgray.png", 0)       # 0 means graey scale

print(im_g, "\n")

print(cv2.imread("smallgray.png", 1))       # 1 menas BGR scale ( other applications use RGB but opencv is ulta )
# The 3 arrays in the above output will represent B G R resp. Each array now represents each pixels's intensity
# for that particular colour.

cv2.imwrite("new_smallgray.png", im_g)      # converting the numy array to an image. 
