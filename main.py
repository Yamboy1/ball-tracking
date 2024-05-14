#!/usr/bin/env python3

import cv2 as cv
from notebook import *

def main():
    file = "multiball"
    path = f'./data/{file}_cropped_610px.mkv'
    capture = readVideoCapture(path)
    print(f"Read file {path}, it has fps of {capture.get(cv.CAP_PROP_FPS)}")
    print("Running background subtractor")
    image_pairs = runBackgroundSubtractor(capture)
    print(f"Writing output file: ./artifacts/{file}.avi")
    writeOutputVideo(f"./artifacts/{file}.avi", 60, image_pairs)
    print("Done :3")


if __name__ == "__main__":
    main()
