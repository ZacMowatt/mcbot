import cv2
import numpy as np
from PIL import ImageGrab


def nothing(x):
    pass


valid = False
live = True

while(not valid)
print("Select Mode:")
print("1. Live Detection")
print("2. Detect From File")

mode = int(input(">"))
if mode == 1 | mode == 2:
    valid = True

showOrigional = True
cv2.namedWindow("Output")

cv2.createTrackbar("Min", "Output", 0, 500, nothing)
cv2.setTrackbarPos("Min", "Output", 70)
cv2.createTrackbar("Max", "Output", 0, 500, nothing)
cv2.setTrackbarPos("Max", "Output", 150)

if live:
    while(True):
        max = cv2.getTrackbarPos("Max", "Output")
        min = cv2.getTrackbarPos("Min", "Output")
        img = ImageGrab.grab(bbox=(500, 240, 1100, 840))
        edges = cv2.Canny(np.array(img), min, max)

        cv2.imshow("Output", edges)

        if showOrigional:
            cv2.imshow("Origional", cv2.cvtColor(
                np.array(img), cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
else:
    img = cv2.imread('screenshot.png', 1)
    edges = cv2.Canny(img, 100, 50)

    cv2.imshow('Origional', img)
    cv2.imshow('Edges', edges)

    print(edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
