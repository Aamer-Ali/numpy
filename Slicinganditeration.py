import cv2

img = cv2.imread("myImage.png", 0)  # This will give Gray Scale becuase of 0 in parametere
print(img)
print()
print(img[0:2])  # Will See First Two rows.
print()
print(img[0:2, 2:4])  # Will See First Two rows and selected index.
print(img.shape)

# The below is an array
# Select Range on the basesof index
#     0    1  2   3   4
# 0 [187 158 104 121 143]
# 1 [198 125 255 255 147]
# 2 [209 134 255  97 182]

print()
# Itteration
for i in img:
    print(i)  # This will itterate thorugh rows

print()
for i in img.T:  # Access the trusposed version of your number
    print(i)  # This will itterate thorugh columns

print()
for i in img.flat:
    print(i)  # This will itterate thorugh number by number
