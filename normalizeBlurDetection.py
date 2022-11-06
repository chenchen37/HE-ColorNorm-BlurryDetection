import imp
import os
import argparse
import numpy as np
from PIL import Image

from normalizeStaining import normalizeStaining
from blurryDetection import varianceLaplacian, fftBlurDetection

if __name__ ==  '__main__':

    # Both normalize and blurry detection
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--patchDir', type=str, help='directory to patches')
    parser.add_argument('--saveDir', type=str, help='directory to save normalized, non-blurry patches')
    parser.add_argument('--saveHE', type=str, default='no', help='whether to save H, E patches. If not, only save normalized patches.')
    parser.add_argument('--normIo', type=int, default=240)
    parser.add_argument('--normAlpha', type=float, default=1.0)
    parser.add_argument('--normBeta', type=float, default=0.15)
    parser.add_argument('--laplacianKsize', type=int, default=13)
    parser.add_argument('--fftSize', type=int, default=0)
    parser.add_argument('--fftThreshold', type=float, default=0.)
    args = parser.parse_args()

