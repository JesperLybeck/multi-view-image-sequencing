import cv2 as cv
from matplotlib import image
import numpy as np
class Processor:
    def __init__(self):
        pass
    def grayScale(self,images):
        if isinstance(images, np.ndarray):
            
            return cv.cvtColor(images, cv.COLOR_BGR2GRAY)
            
        else:
            return [cv.cvtColor(image, cv.COLOR_BGR2GRAY) for image in images]
            
    
    def resize(self,images,scale):
        if isinstance(images, np.ndarray):
            
            return cv.resize(images, (0,0), fx=scale, fy=scale)
            
        else:
            
            return [cv.resize(image, (0,0), fx=scale, fy=scale) for image in images]
    
    def histogramNormalization(self,images):
        if isinstance(images, np.ndarray):
            return cv.equalizeHist(images)
    
            
        else:
            return [cv.equalizeHist(image) for image in images]   
            
    def CLAHE(self,images,clipLimit=2.0,tileGridSize=(8,8)):
        if isinstance(images, np.ndarray):
            
            clahe = cv.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
            return clahe.apply(images)
        else:
            clahe = cv.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
            return [clahe.apply(image) for image in images]