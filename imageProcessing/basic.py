import cv2 as cv

img = cv.imread('../resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# #converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scale', gray)

# #Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# #edge cascade
# edge = cv.Canny(blur, 125, 175)
# cv.imshow('Edges', edge)

# #dilating the image
# dilated = cv.dilate(edge, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# #Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#cropping
crop = img[50:200, 200:400]
cv.imshow('Cropped', crop)


cv.waitKey(0)