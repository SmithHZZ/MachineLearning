import cv2

img = cv2.imread('../images/lena_color.tiff')

cv2.imshow("img", img)

cv2.waitKey(0)
