import cv2
import numpy as np
from PIL import Image
import os
img=cv2.imread("images\original.jpg")
imag = Image.open("images\original.jpg")
# r,thresh1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# # adap=cv2.adaptiveThreshold(img, 192,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_MEAN_C,11,12)

# cv2.imshow('Threshold', thresh1)
# cv2.imshow('Org',img)
# # cv2.imshow('Adap',adap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np

# dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# img=cv2.imread("/content/emotions/images/images/train/angry/0.jpg")
  # noice=cv2.add(image_res,gauss_noise)
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(img, 1.3, 5)
print(faces[0])
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    img2 = face = img[y:y + h, x:x + w]

cv2.imwrite('detected..jpg', img)
cv2.imwrite('croped.jpg', img2)
graying = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imwrite('graying.jpg',graying)
# thresh1 =cv2.threshold(histo,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(graying,kernel,iterations = 1)
cv2.imwrite('erosion.jpg', erosion)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
cv2.imwrite('diluted.jpg', dilation)
histo=cv2.equalizeHist(dilation)
cv2.imwrite('histo.jpg', histo)
cv2.imshow('Threshold', histo)
cv2.imshow('Org',img)
cv2.imshow('img',img)
cv2.imshow('crop',img2)
# cv2.imshow('Adap',adap)
cv2.waitKey(0)
cv2.destroyAllWindows()
