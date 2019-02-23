import cv2
import numpy as np

MainHeader = '''
┏━┓╺┳╸┏━╸┏━╸┏━┓┏┓╻┏━┓┏━╸┏━┓┏━┓┏━┓╻ ╻╻ ╻       Hide an Image within another
┗━┓ ┃ ┣╸ ┃╺┓┣━┫┃┗┫┃ ┃┃╺┓┣┳┛┣━┫┣━┛┣━┫┗┳┛                   by
┗━┛ ╹ ┗━╸┗━┛╹ ╹╹ ╹┗━┛┗━┛╹┗╸╹ ╹╹  ╹ ╹ ╹                @mhsattarian
'''
print(MainHeader)

image1 = cv2.imread('image.jpeg', 0)
image2 = cv2.imread('image2.png', 0)

def getMSBs(number, numberOfBits = 4):
  a = number >> numberOfBits
  b = a << numberOfBits
  return b

def setMSBasLSB (number, numberOfBits = 4):
  a = number >> numberOfBits
  # b = a << numberOfBits
  return a

def compressImage(image, reverse = False):
  h, w = image.shape
  out = np.zeros([h,w], dtype=np.uint8)

  for i in range(h):
    for j in range(w):
      temp = getMSBs(image[i, j])
      if reverse: temp = setMSBasLSB(temp)
      out[i, j] = temp
  return out

def encodeImageInImage(image1, image2):
  o1 = compressImage(image1)
  o2 = compressImage(image2, True)

  cv2.imshow("1"*100, o1)
  cv2.waitKey(0)
  cv2.imshow("2"*100, o2)
  cv2.waitKey(0)
  
  return o1 | o2


out = encodeImageInImage(image1, image2)
cv2.imshow("3"* 100, out)
cv2.waitKey(0)
cv2.destroyAllWindows()
