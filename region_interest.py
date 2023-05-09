import cv2
import numpy as np

img=cv2.imread("images\\5.jpg")
img=cv2.resize(img,(512,512))
img2=cv2.imread("images\\1.jpg")
img2=cv2.resize(img2,(512,512))
r=cv2.selectROI("select the area", img2)
print(r)
cv2.imshow('or operation', r)
cv2.imshow('orginal', img2)
cropped_image = img2[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]
cv2.imshow('and operation', cropped_image)


cv2.waitKey(0)
cv2.destroyAllWindows()