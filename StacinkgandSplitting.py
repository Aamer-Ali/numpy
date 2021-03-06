import cv2
import numpy
myimg =cv2.imread("myImage.png",0)
print(myimg)


# While Stacking an Array make sure all have same dimensions otherwise it will through an error
# Stacking of an array
# There are two Stack hstack (Horizontal Stack) and vstack (Vertical Stack)
print()
print("Horizontal Stacked Array :")
myStack = numpy.hstack((myimg,myimg)) # if you want you can add more arrays
print(myStack)

print()
print("Vertical Stacked Array :")
myStack = numpy.vstack((myimg,myimg)) # if you want you can add more arrays
print(myStack)


# Splitting means deviding an array into small parts
# There are also hSplit and vsplit
print()
print("Horizontal Splitting Stack")
myList = numpy.hsplit(myimg,5)
print(myList)

print()
print("Vertical Splitting Stack")
myList = numpy.hsplit(myimg,3)
print(myList)