import cv2 as cv

path = r'C:\Users\student\PycharmProjects\pythonProject_ppl\kurama.jpg'

newpath = r'C:\Users\student\Downloads\kurama2.png'

image = cv.imread(path)
# window_name = 'image'
# cv.imshow("Kep", image)
# cv.waitKey(1000)
# cv.imwrite((newpath, image))
# cv.destroyAllWindows()

result = cv.imwrite(r"C:\Users\student\Downloads\kurama2.jpg", image)
#displaying the return value from the imwrite() function
print("The image is saved to the file : ", result)