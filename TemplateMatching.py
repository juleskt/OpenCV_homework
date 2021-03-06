from __future__ import division
import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0
    var_t = 0
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 

    #averageValuePerRow = np.mean(temp)
    mean_t = temp.mean()
    var_t = np.var(temp)
    
    max_corr = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            corr = 0
            nccSecondHalf = 0
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            windowSlice = src[i:i+src.shape[0], j:j+src.shape[1]]

            mean_s = windowSlice.mean()
            var_s = np.var(windowSlice)
            
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            corr = (1 / temp.shape[0] * temp.shape[1])

            for row in range (temp.shape[0]):
                for col in range (temp.shape[1]):
                    nccSecondHalf += (temp[row,col] - mean_t) * (windowSlice[row,col] - mean_s)
            
            nccSecondHalf /= (var_t * var_s)
            corr *= nccSecondHalf

            if corr > max_corr:
                max_corr = corr
                location = [i, j]
    return location

# load source and template images
source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
temp = cv2.imread('template_img.jpg',0) # read image in grayscale

location = TemplateMatching(source_img, temp, 20)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
cv2.rectangle(match_img, (location[1], location[0]), (location[1]+temp.shape[1],location[0]+temp.shape[0]), (0,0,255), 2)

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
cv2.imwrite('matched_output.jpg', match_img)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()