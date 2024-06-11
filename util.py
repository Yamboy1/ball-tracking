import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def readFramesFromFile(path, frameCount):
    """ Read a specific number of frames from the video file at `path` """

    capture = cv.VideoCapture(cv.samples.findFileOrKeep(path))

    if not capture.isOpened():
        raise Exception("Couldn't open file")

    frames = []
    for _ in range(frameCount):
        ret, frame = capture.read()
        if not ret:
            break
        frames.append(frame)

    return np.array(frames)

def displayImagePair(imagePair):
    """ Helper function to display a (image,mask)
        pair in a notebook using matplotlib """
    image, mask = imagePair
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    frame = np.concatenate((image, mask), axis=1)
    plt.imshow(frame)

def writeOutputVideo(path, fps, frames):
    """ Write an output video to the given path in avi format with a specific
        fps using the (blurred, rawMask, thresholdMask, contour) tuple,
        displaying only the contour output """
    _, height, width, *_ = frames.shape
    video_dims = (width, height)
    video_writer = cv.VideoWriter(path, cv.VideoWriter_fourcc(*'XVID'), fps, video_dims)
    for frame in frames:
        video_writer.write(frame)
    video_writer.release()
