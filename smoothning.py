import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats', img)

#Averaging 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Image', bilateral)

cv.waitKey(0)