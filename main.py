#!/usr/bin/env python3

import cv2 as cv
from notebook import *

def main():
    file = "multiball"
    path = f'./data/{file}_cropped_610px.mkv'
    capture = readVideoCapture(path)
    print(f"Read file {path}, it has fps of {capture.get(cv.CAP_PROP_FPS)}")
    frames = readFrames(capture, 2000)
    print("2000 frames read :)")
    print("Running background subtractor")
    image_pairs = runBackgroundSubtractor(frames, 15)
    output_filename = f"./artifacts/{file}-medianblur-{size}.avi"
    print(f"Writing output file: {output_filename}")
    writeOutputVideo(output_filename, 60, image_pairs)
    print("Done :3")


if __name__ == "__main__":
    main()
