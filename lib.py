import cv2 as cv
import numpy as np
from imutils.video import FPS

backSub = cv.createBackgroundSubtractorMOG2(detectShadows=True)

def readVideoCapture(path):
    capture = cv.VideoCapture(cv.samples.findFileOrKeep(path))
    if not capture.isOpened():
        raise Exception("Couldn't open file")
    return capture

def applyGaussianBlur(frames, size):
    output = []
    for frame in frames:
        blurred = cv.GaussianBlur(frame, (size, size), 0)
        output.append(blurred)
    return np.array(output)

def applyMedianBlur(frames, size):
    output = []
    for frame in frames:
        blurred = cv.medianBlur(frame, size)
        output.append(blurred)
    return np.array(output)

def readFrames(capture, frameCount):
    frames = []
    for _ in range(frameCount):
        ret, frame = capture.read()
        if not ret:
            break
        frames.append(frame)
    return np.array(frames)


def runBackgroundSubtractor(frames, kernelSize):
    blurred = applyGaussianBlur(frames, kernelSize)
    image_pairs = []
    for i, blurFrame in enumerate(blurred):
        fgMask = backSub.apply(blurFrame)
        ret , threshold = cv.threshold(fgMask.copy(), 230, 255,cv.THRESH_BINARY)
        dilated = cv.dilate(threshold,cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3)),iterations = 2)
        contours, hierarchy = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contourFrame = frames[i]
        cv.drawContours(contourFrame, contours, -1, (0,255,0), 3)
        maskFrame = cv.cvtColor(dilated, cv.COLOR_GRAY2RGB)
        pureMaskFrame = cv.cvtColor(fgMask, cv.COLOR_GRAY2RGB)
        image_pairs.append((blurFrame, pureMaskFrame, maskFrame, contourFrame))
    return np.array(image_pairs)

def display_imagepair(index):
    image, mask = image_pairs[index]
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    frame = np.concatenate((image, mask), axis=1)
    plt.imshow(frame)

def writeOutputVideo(path, fps, image_pairs):
    video_dim = (610, 1080)
    video_writer = cv.VideoWriter(path, cv.VideoWriter_fourcc(*'XVID'), fps, video_dim)
    for image_pair in image_pairs:
        combined_frame = np.concatenate(image_pair, axis=1)
        video_writer.write(image_pair[3])
    video_writer.release()

