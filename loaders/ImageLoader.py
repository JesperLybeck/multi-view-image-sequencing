import numpy as np
import os
import cv2 as cv

from config.ImageData import ImageData

class ImageLoader:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def __init__(self):
        pass

    def loadEasyUpper(self,file_path = "./data/easy",modality="rgb",imageFormat = "png",maxImages = None) -> list[ImageData]:
        folder = os.path.join(self.BASE_DIR, file_path, "upper_loop", modality)
        if maxImages is None:
            print(f"Loading all images from {folder}")
            return [cv.imread(os.path.join(folder, f)) for f in os.listdir(folder) if f.endswith('.' + imageFormat)]
        else:
            files = [f for f in os.listdir(folder) if f.endswith('.' + imageFormat)]
            print(f"Loading {len(files[:maxImages])} images from {folder}")
            return [cv.imread(os.path.join(folder, f)) for f in files[:maxImages]]

    def loadEasyLower(self,file_path = "/data/easy",modality = "rgb") -> list[ImageData]:
        pass
    def loadEasyFull(self,file_path = "/data/easy",modality = "rgb") -> list[ImageData]:
        pass

    