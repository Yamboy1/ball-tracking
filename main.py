#!/usr/bin/env python3

import cv2 as cv
from lib import *

def main():
    file = "multiball"
    path = f'./data/{file}_cropped_610px.mkv'
    num_frames = 1500
    capture = readVideoCapture(path)
    print(f"Read file {path}, it has fps of {capture.get(cv.CAP_PROP_FPS)}")
    frames = readFrames(capture, num_frames)
    print("1500 frames read :)")
    print("Running background subtractor")
    image_pairs = runBackgroundSubtractor(frames, 15)
    del frames
    output_filename = f"./artifacts/{file}-shadows-15.avi"
    print(f"Writing output file: {output_filename}")
    writeOutputVideo(output_filename, 60, image_pairs)
    print("Done :3")


if __name__ == "__main__":
    main()
