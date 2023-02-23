import cv2 as cv

path = r'C:\Users\student\PycharmProjects\pythonProject_ppl\kurama.jpg'

# newpath = r'C:\Users\student\Downloads\kurama2.png'

image = cv.imread(path)
# window_name = 'image'
cv.imshow("Kep", image)
cv.waitKey(1000)
for x in range(1024):
    for y in range(756):
        image[y,x][0]=255
cv.imshow("Kep", image)
cv.waitKey(0)
# cv.imwrite((newpath, image))
# cv.destroyAllWindows()