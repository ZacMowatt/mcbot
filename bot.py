import cv2
import numpy as np

img = cv2.imread('screen.png',0)
edges = cv2.Canny(img,100,200)

cv2.imshow('Origional', img)
cv2.imshow('Edges', edges)

plt.show()