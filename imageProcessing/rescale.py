import cv2 as cv

#reading images
img = cv.imread('../resources/Photos/cat.jpg')
cv.imshow("Cat", img)

def rescaleFrame(frame, scale=1.75):
    #works for images, videoas and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow("Resized image", resized_image)
cv.waitKey(0)

def changeRes(width, height):
    #works for Live videos
    capture.set(3, width)
    capture.set(4, height)

#reading videos
capture = cv.VideoCapture('../resources/Videos/diceVideo.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("resized Video", frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()