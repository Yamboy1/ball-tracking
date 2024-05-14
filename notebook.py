import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorMOG2()

def readVideoCapture(path):
    capture = cv.VideoCapture(cv.samples.findFileOrKeep(path))
    if not capture.isOpened():
        raise Exception("Couldn't open file")
    return capture


def runBackgroundSubtractor(capture):
    image_pairs = []
    for _ in range(2000):
        ret, frame = capture.read()
        if frame is None:
            break
        fgMask = backSub.apply(frame)
        maskFrame = cv.cvtColor(fgMask, cv.COLOR_GRAY2RGB)
        image_pairs.append((frame, maskFrame))
    return image_pairs

def display_image_pair(index):
    image, mask = image_pairs[index]
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    frame = np.concatenate((image, mask), axis=1)
    plt.imshow(frame)

def writeOutputVideo(path, fps, image_pairs):
    video_dim = (1220, 1080)
    video_writer = cv.VideoWriter(path, cv.VideoWriter_fourcc(*'XVID'), fps, video_dim)
    for image_pair in image_pairs:
        combined_frame = np.concatenate(image_pair, axis=1)
        video_writer.write(combined_frame)
    video_writer.release()

