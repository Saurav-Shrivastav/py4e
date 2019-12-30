import cv2

im_g = cv2.imread("smallgray.png", 0)

print("The size of the array is:",im_g.shape, "\n")   # gives you the size of the array
print(im_g[1:3, 2:4], "\n")

# iterating
for i in im_g:
    print(i)    # Will print out the rows.
print("")
for i in im_g.T:
    print(i)    # To print out the columns
for i in im_g.flat:
    print(i)    # To get all the numbers
