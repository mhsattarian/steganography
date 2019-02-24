#!/usr/bin/python3
import cv2
import numpy as np

class Steganography:

  def __init__(self, imageColorBits = 8):
    # Assume Images have 8 bit to store colors
    self.imageColorBits = imageColorBits

  def compress_image(self, image, setLowOrder = False, numberOfBits = 4):
    """Compress image by removing low-order bits"""
    numberOfBits = self.imageColorBits - numberOfBits
    imageShiftedRight = np.right_shift(image, numberOfBits)
    if not setLowOrder: return np.left_shift(imageShiftedRight, numberOfBits)
    else: return imageShiftedRight

  def encode_images(self, image1, image2):
    if type(image1) == 'str': image1 = cv2.imread(image1)
    if type(image2) == 'str': image2 = cv2.imread(image2)
    
    container = self.compress_image(image1)
    containee = self.compress_image(image2, setLowOrder = True)
    
    return container | containee

  def decode_image(self, image, numberOfBits = 4):
    numberOfBits = self.imageColorBits - numberOfBits
    codedImage = np.bitwise_and(image, pow(2, numberOfBits) - 1)
    return np.left_shift(codedImage, numberOfBits)
    

if __name__ == '__main__':
  MainHeader = '''
  ┏━┓╺┳╸┏━╸┏━╸┏━┓┏┓╻┏━┓┏━╸┏━┓┏━┓┏━┓╻ ╻╻ ╻       Hide an Image within another
  ┗━┓ ┃ ┣╸ ┃╺┓┣━┫┃┗┫┃ ┃┃╺┓┣┳┛┣━┫┣━┛┣━┫┗┳┛                   by
  ┗━┛ ╹ ┗━╸┗━┛╹ ╹╹ ╹┗━┛┗━┛╹┗╸╹ ╹╹  ╹ ╹ ╹                @mhsattarian

  '''
  print(MainHeader)


  container = cv2.imread('images/container.png')
  containee = cv2.imread('images/containee.png')

  s = Steganography()
  output = s.encode_images(container, containee)
  cv2.imwrite("images/output.png", output)
  
  codedImage = s.decode_image(output)
  cv2.imwrite("images/coded.png", codedImage)

  print("- output stored in Images directory.")

  # cv2.imshow("container", container)
  # cv2.waitKey(0)
  # cv2.imshow("containee", containee)
  # cv2.waitKey(0)
  # cv2.imshow("output", output)
  # cv2.waitKey(0)
  
  # cv2.destroyAllWindows()
