import cv2
import numpy as np
from steganography import Steganography
from tqdm import tqdm

image = cv2.imread('images/container.png', 0)
s = Steganography()

for i in tqdm(range(9)):
  output = s.compress_image(image=image, numberOfBits = i)
  cv2.imwrite(f"images/extracted_images/image using {i} bit.png", output)
