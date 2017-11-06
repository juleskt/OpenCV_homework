import cv2
import sys
 
def addGaussianNoise(img, mean, sigma):
    newImg = img.copy()
    noiseImage = img.copy()
    rng = cv2.CV_RNG().fill(noiseImage, 1, mean, sigma)
    return newImg

def addSaltAndPepperNoise(src, pa, pb):
    img = src.copy()
    amountOne = img.rows * img.cols * pa
    amountTwo = img.rows * img.cols * pb

    for x in range(0, amountOne):
        img[(cv2.CV_RNG().uniform(0, img.rows)), cv2.CV_RNG().uniform(0, img.cols))] = 0

    for x in range(0, amountTwo):
        img[(cv2.CV_RNG().uniform(0, img.rows)), cv2.CV_RNG().uniform(0, img.cols))] =0

    return img

src = cv2.imread(sys.argv[1], 0)
cv2.imshow("Original Image", src)

noisyImg = addGaussianNoise(src, 0, 50)
cv2.imshow("Gaussian Noise", noisyImg)

noiseDst = cv2.blur(noisyImg.copy(),(3,3))
imshow("Box filter", noiseDst)

noiseDst1 = cv2.GaussianBlur(noisyImg.copy(), (3,3), 1.5)
imshow("Gaussian Filter", noiseDst1)

noiseDst2 = cv2.medianBlur(noisyImg.copy(), 3)
imshow("Median Filter", noiseDst2)


noisyImg2 = addSaltAndPepperNoise(src, .01, .01)
imshow("Salt and Pepper Noise", noisyImg2)

noiseDst = cv2.blur(noisyImg2.copy(),(3,3))
imshow("Box filter", noiseDst)

noiseDst1 = cv2.GaussianBlur(noisyImg2.copy(), (3,3), 1.5)
imshow("Gaussian Filter", noiseDst1)

noiseDst2 = cv2.medianBlur(noisyImg2.copy(), 3)
imshow("Median Filter", noiseDst2)