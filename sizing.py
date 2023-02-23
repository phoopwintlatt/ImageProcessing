import cv2 as cv
import numpy as np

path = r'C:\Users\student\PycharmProjects\pythonProject_ppl\kurama.jpg'

# newpath = r'C:\Users\student\Downloads\kurama2.png'

image = cv.imread(path)

newimage = np.zeros((200,300,3))
# black image by numpy

cv.imshow("Kep", newimage)
cv.waitKey(1000)
