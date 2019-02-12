import cv2

# Reading a iamge file in the form of matrix
img = cv2.imread("myImage.png")
print(img)

# Writing an array to create an Image file
# we have the variable "img" in array form we will use that to create a new image

cv2.imwrite("myNewImage.png",img) #After executing this code we will have new image in our project folder
