import cv2
import sys
 
src = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
# Assuming (20,25) means x = 20, y = 25, numpy indices are inversed

cv2.imshow("Original Image", src)

b,g,r = cv2.split(src)
print "BGR:"
print b[25,20]
print g[25,20]
print r[25,20]
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

srcYCC = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
Y,Cb,Cr = cv2.split(srcYCC)
print "\nYCC:"
print Y[25,20]
print Cb[25,20]
print Cr[25,20]
cv2.imshow("Y", Y)
cv2.imshow("Cb", Cb)
cv2.imshow("Cr", Cr)

srcHSV = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)
H,S,V = cv2.split(srcHSV)
print "\nHSV:"
print H[25,20]
print S[25,20]
print V[25,20]
cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)

cv2.waitKey(0)