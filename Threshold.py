import cv2
import sys

src = cv2.imread(sys.argv[1], 1)
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imshow("Input Image", src)

threshValue = 128

ret,thresh1 = cv2.threshold(gray, threshValue, 255, cv2.THRESH_TRUNC)
cv2.imshow("Thresholded Image", thresh1)

ret,thresh2 = cv2.threshold(gray, threshValue, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Threshold", thresh2)

ret,thresh3 = cv2.threshold(gray, 27, 125, cv2.THRESH_BINARY)
ret,thresh4 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Band Thresholding", cv2.bitwise_and(thresh3, thresh4))

ret,thresh5 = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Semi Thresholding", cv2.bitwise_and(gray, thresh5))

thresh6 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
cv2.imshow("Adaptive Thresholding", thresh6)

cv2.waitKey(0)