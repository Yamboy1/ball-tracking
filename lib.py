import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorMOG2(detectShadows=True)

def runBackgroundSubtractor(frame, kernelSize):
    blurFrame = cv.GaussianBlur(frame, (kernelSize, kernelSize), 0)
    fgMask = backSub.apply(blurFrame)
    # Filter out shadows. The background subtractor detects shadows
    # and displays them with a lower value in the grayscale image.
    # 230 is a value that appears to work here, but no guarantees.
    _, threshold = cv.threshold(fgMask, 254, 255, cv.THRESH_BINARY)
    # Not sure why I'm doing this, maybe it's useful, maybe i want to erode it instead?
    # See https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/
    # for more information on dilation and erosion :)
    #dilated = cv.dilate(threshold, cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3)), iterations=2)
    eroded = cv.erode(threshold, None, iterations=2)
    dilated = eroded
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, contours, -1, (0,0,255), 3)
    mask = cv.cvtColor(fgMask,cv.COLOR_GRAY2BGR)
    predilateMask = cv.cvtColor(threshold,cv.COLOR_GRAY2BGR)
    thresholdMask = cv.cvtColor(dilated,cv.COLOR_GRAY2BGR)
    return np.concatenate((frame, mask, predilateMask, thresholdMask), axis=1)
