import cv2
import numpy as np

def varianceLaplacian(image, ksize=13):
    '''
    Input: image array (gray scale)
    Output: variance of Laplacian
    '''
    return cv2.Laplacian(image, cv2.CV_64F, ksize=ksize).var()

def fftBlurDetection(image, size, thresh):
    h, w = image.shape
    cX, cY = int(w/2.), int(h/2.)
    
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)
    
    fftShift[cY - size:cY + size, cX - size:cX + size] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)
    
    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    
    return mean, (mean<=thresh)

