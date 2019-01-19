#!/usr/bin/env python3
import sys
import numpy as np

with open(sys.argv[1], 'r') as my_file:
    pixels = my_file.read().split('\n')[:-1]

firstDist = float(sys.argv[2])
[print(i) for i in np.array(pixels).astype(np.float32) * firstDist / (float(pixels[1]) - float(pixels[0]))]
