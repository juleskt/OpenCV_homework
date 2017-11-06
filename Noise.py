import cv2
import sys
import numpy as np
 
def addGaussianNoise(img, mean, sigma):
    newImg = img.copy()
    noiseImage = np.zeros(img.shape, np.uint8)
    cv2.randn(noiseImage, mean, sigma)
    return cv2.add(newImg, noiseImage)

def addSaltAndPepperNoise(src, pa, pb):
    rnd = np.random.rand(src.shape[0], src.shape[1])
    noiseImage = src.copy()

    noiseImage[rnd < pa] = 0
    noiseImage[rnd > 1 - pa] = 1

    noiseImage[rnd > 1 - pb] = 255

    return noiseImage

src = cv2.imread(sys.argv[1], 0)
cv2.imshow("Original Image", src)

noisyImg = addGaussianNoise(src, 0, 50)
cv2.imshow("Gaussian Noise", noisyImg)

noiseDst = cv2.blur(noisyImg.copy(),(3,3))
cv2.imshow("GBox filter", noiseDst)

noiseDst1 = cv2.GaussianBlur(noisyImg.copy(), (3,3), 1.5)
cv2.imshow("GGaussian Filter", noiseDst1)

noiseDst2 = cv2.medianBlur(noisyImg.copy(), 3)
cv2.imshow("GMedian Filter", noiseDst2)


noisyImg2 = addSaltAndPepperNoise(src, .01, .01)
cv2.imshow("Salt and Pepper Noise", noisyImg2)

noiseDst = cv2.blur(noisyImg2.copy(),(3,3))
cv2.imshow("Box filter", noiseDst)

noiseDst1 = cv2.GaussianBlur(noisyImg2.copy(), (3,3), 1.5)
cv2.imshow("Gaussian Filter", noiseDst1)

noiseDst2 = cv2.medianBlur(noisyImg2.copy(), 3)
cv2.imshow("Median Filter", noiseDst2)

cv2.waitKey(0)