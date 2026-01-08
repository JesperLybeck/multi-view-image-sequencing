import cv2 as cv
import matplotlib
from preprocessing.pre_processor import Processor
from loaders.ImageLoader import ImageLoader
from config.ImageData import ImageData
import os
import sys
from plotting.Plotter import Plotter

import numpy as np
import matplotlib.pyplot as plt


def main():
    print("hello")
    loader = ImageLoader()
    imgs = loader.loadEasyUpper(maxImages=5)
    processor = Processor()
    plotter = Plotter()
    print("images loaded!")
    # example: call loader using a path relative to Project/
   
    print("Loaded", len(imgs), "images")
    originalImage = processor.resize(imgs[0], 0.5)
    grayscaleImage = processor.grayScale(originalImage)
    histogramNormalizedImage = processor.histogramNormalization(grayscaleImage)
    CLAHEImage = processor.CLAHE(grayscaleImage)
    
    
    plotter.plot_comparison_with_hist(originalImage, grayscaleImage, histogramNormalizedImage, CLAHEImage, save_path="preprocessing_comparison.png")
    
    
    


main()