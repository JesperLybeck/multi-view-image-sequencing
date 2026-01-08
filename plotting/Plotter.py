import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
class Plotter:
    def __init__(self):
        pass

    def plotImage(self, image: np.ndarray, title: str | None = None)-> None:
        
        if image.ndim == 2:  # grayscale
            plt.imshow(image, cmap="gray")
        else:  # RGB
            plt.imshow(image)
        plt.show()

    def saveImage(self, image, file_name: str) -> None:
        print(type(image), getattr(image, "shape", None))
        cv.imwrite(f"{file_name}", image)
        print(f"Image saved as {file_name}")


    def __init__(self):
        pass

import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        pass

    def plotImage(self, image: np.ndarray, title: str | None = None) -> None:
        img = np.asarray(image)
        if img.ndim == 2:  # grayscale
            plt.imshow(img, cmap="gray")
        else:  # assume BGR -> convert to RGB for matplotlib
            plt.imshow(img[..., ::-1])
        if title:
            plt.title(title)
        plt.axis("off")
        plt.show()

    def saveImage(self, image, file_name: str) -> bool:
        img = np.asarray(image)
        if np.issubdtype(img.dtype, np.floating):
            img = (255 * np.clip(img, 0.0, 1.0)).astype(np.uint8)
        else:
            img = img.astype(np.uint8)

        # convert RGB->BGR for OpenCV if needed
        if img.ndim == 3 and img.shape[2] == 3:
            img_to_write = img[..., ::-1]
        else:
            img_to_write = img

        abs_path = os.path.abspath(file_name)
        out_dir = os.path.dirname(abs_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        ok = cv.imwrite(abs_path, img_to_write)
        print(f"saveImage: wrote={ok} path={abs_path}")
        return bool(ok)



    # ...existing code...
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        pass

    def plotImage(self, image: np.ndarray, title: str | None = None)-> None:
        img = np.asarray(image)
        if img.ndim == 2:  
            plt.imshow(img, cmap="gray")
        else:  
           
            plt.imshow(img[..., ::-1])
        if title:
            plt.title(title)
        plt.axis("off")
        plt.show()

    def saveImage(self, image, file_name: str) -> None:
        img = np.asarray(image)
        if np.issubdtype(img.dtype, np.floating):
            img = (255 * np.clip(img, 0.0, 1.0)).astype(np.uint8)
        else:
            img = img.astype(np.uint8)
        abs_path = os.path.abspath(file_name)
        out_dir = os.path.dirname(abs_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        
        if img.ndim == 3 and img.shape[2] == 3:
            img_to_write = img[..., ::-1]
        else:
            img_to_write = img
        ok = cv.imwrite(abs_path, img_to_write)
        print(f"saveImage: wrote={ok} path={abs_path}")
        return ok

    
   