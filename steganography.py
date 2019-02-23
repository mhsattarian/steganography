import cv2
import numpy as np

image = cv2.imread('image.jpeg', 0)

def getMSBs(number, numberOfBits = 4):
  numberOfBits = 8 - numberOfBits
  a = number >> numberOfBits
  b = a << numberOfBits
  return b

def compressImage(image, numberOfBits = 4):
  h, w = image.shape
  out = np.zeros([h,w], dtype=np.uint8)

  for i in range(h):
    for j in range(w):
      out[i, j] = getMSBs(image[i, j], numberOfBits)
  return out

for i in range(8):
  img = compressImage(image, i)
  cv2.imwrite(f"output/image-{i}.png", img)


# out = encodeImageInImage(image1, image2)
# cv2.imshow(" "*100, image1)
# cv2.waitKey(0)
# cv2.imshow(" "*100, image2)
# cv2.waitKey(0)
# cv2.imshow(" "* 100, out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
