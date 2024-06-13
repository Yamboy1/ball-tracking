#!/usr/bin/env python3

import sys
import cv2 as cv
from lib import runBackgroundSubtractor
from util import *

def main():
    if len(sys.argv) <= 1:
        print("Please pass in an input file!")
        exit(1)
    file = sys.argv[1]
    path = f'./data/{file}'
    kernelSize = 15
    numFrames = 1500
    print(f"Reading {numFrames} frames from file {path}...")
    frames = readFramesFromFile(path, numFrames)
    print("Running background subtractor...")
    outputFrames = []
    for frame in frames:
        outputFrames.append(runBackgroundSubtractor(frame, kernelSize))
    outputFrames = np.array(outputFrames)
    name = input("Give a name to this output: ")
    outputFilename = f"./artifacts/{file}-{name}.avi"
    print(f"Writing output file: {outputFilename}...")
    print(f"Shape: {outputFrames.shape}")
    writeOutputVideo(outputFilename, 60, outputFrames)
    print("Done :3")


if __name__ == "__main__":
    main()
