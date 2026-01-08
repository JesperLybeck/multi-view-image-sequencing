
from dataclasses import dataclass
import numpy as np

@dataclass
class ImageData:
    image: np.ndarray
    name: str
    modality: str = "RGB"
    