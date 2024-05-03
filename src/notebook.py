#!/usr/bin/env python

import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorMOG2()
blurredBackSub = cv.createBackgroundSubtractorMOG2()

file = "multiball"
# file = "half_hour"
capture = cv.VideoCapture(cv.samples.findFileOrKeep(f'../data/{file}_cropped_610px.mkv'))

if not capture.isOpened():
    print('Unable to open file')
    exit(0)

image_pairs = []
for _ in range(2000):
    ret, frame = capture.read()
    if frame is None:
        break
    fgMask = backSub.apply(frame)
    maskFrame = cv.cvtColor(fgMask, cv.COLOR_GRAY2RGB)
    image_pairs.append((frame, maskFrame))

IMAGE = 0
MASK = 1

def display_image_pair(index):
    image, mask = image_pairs[index]
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    frame = np.concatenate((image, mask), axis=1)
    plt.imshow(frame)

#display_image_pair(100)
#display_image_pair(200)
#display_image_pair(300)
#display_image_pair(400)
#display_image_pair(500)
#display_image_pair(600)

fps = 50
video_dim = (1220, 1080)
video_writer = cv.VideoWriter(f"../artifacts/{file}.avi", cv.VideoWriter_fourcc(*'XVID'), fps, video_dim)
for image_pair in image_pairs:
    combined_frame = np.concatenate(image_pair, axis=1)
    video_writer.write(combined_frame)
video_writer.release()

