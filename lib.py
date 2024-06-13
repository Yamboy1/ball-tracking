import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorMOG2(detectShadows=True)

def runBackgroundSubtractor(frame, kernelSize):
    blurFrame = cv.GaussianBlur(frame, (kernelSize, kernelSize), 0)
    fgMask = backSub.apply(blurFrame)
    # Filter out shadows. The background subtractor detects shadows
    # and displays them with a lower value in the grayscale image.
    # Shadows are anything below 255, so we set the threshold to be 254.
    _, threshold = cv.threshold(fgMask, 254, 255, cv.THRESH_BINARY)
    # With some trial and error, it looks like a circular kernel of size 4
    # seems to work best, along with an opening with 3 iterations. 4 iterations
    # was cutting out slightly more frames of the ball than I would have liked.
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(4,4))
    opening = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel, iterations=3)

    contours, _ = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, contours, -1, (0,0,255), 3)
    mask = cv.cvtColor(fgMask,cv.COLOR_GRAY2BGR)
    openingMask = cv.cvtColor(opening, cv.COLOR_GRAY2BGR)
    return np.concatenate((frame, openingMask), axis=1)
