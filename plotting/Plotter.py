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
        if img.ndim == 2:  # grayscale
            plt.imshow(img, cmap="gray")
        else:  # RGB/BGR
            # assume OpenCV BGR -> convert to RGB for matplotlib
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
        # convert RGB->BGR if needed for OpenCV write
        if img.ndim == 3 and img.shape[2] == 3:
            img_to_write = img[..., ::-1]
        else:
            img_to_write = img
        ok = cv.imwrite(abs_path, img_to_write)
        print(f"saveImage: wrote={ok} path={abs_path}")
        return ok

    
    def plot_comparison_with_hist(self, original, grayscale, global_norm, clahe, bins: int = 256, save_path: str | None = None):
        
        imgs = [original, grayscale, global_norm, clahe]
        titles = ["Original", "Grayscale", "Global Normalized", "CLAHE"]

        fig, axes = plt.subplots(
        2, 4,
        figsize=(18, 6), 
        gridspec_kw={'height_ratios': [6, 1]},
        constrained_layout=True
        
            )
        fig.suptitle("Preprocessing and Histogram Comparison", fontsize=18)
        for i, img in enumerate(imgs):
            ax = axes[0, i]
            arr = np.asarray(img)
            
            if arr.ndim == 3 and arr.shape[2] == 3:
                ax.imshow(arr[..., ::-1])
            else:
                ax.imshow(arr, cmap="gray")
            ax.set_title(titles[i])
            ax.axis("off")

            
            if arr.ndim == 3 and arr.shape[2] == 3:
                gray = cv.cvtColor(arr, cv.COLOR_BGR2GRAY)
            else:
                gray = arr

           
            gray_u8 = np.asarray(gray).astype(np.uint8)

           
            hist = cv.calcHist([gray_u8], [0], None, [bins], [0, 256]).ravel()
            edges = np.linspace(0, 256, bins + 1)

            axh = axes[1, i]
            axh.plot(edges[:-1], hist, color="k")
            axh.fill_between(edges[:-1], hist, color="lightgray")
            axh.set_xlim(0, 255)
            axh.set_xlabel("Intensity")
            axh.set_ylabel("Count")
            axh.set_title(f"{titles[i]} histogram")

        plt.tight_layout()
        if save_path:
            abs_path = os.path.abspath(save_path)
            out_dir = os.path.dirname(abs_path)
            if out_dir:
                os.makedirs(out_dir, exist_ok=True)
            fig.savefig(abs_path, dpi=150)
            print("Saved comparison figure to", abs_path)
        plt.show()
