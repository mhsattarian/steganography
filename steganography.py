#!/usr/bin/python3
import cv2
import numpy as np

MainHeader = '''
┏━┓╺┳╸┏━╸┏━╸┏━┓┏┓╻┏━┓┏━╸┏━┓┏━┓┏━┓╻ ╻╻ ╻       Hide an Image within another
┗━┓ ┃ ┣╸ ┃╺┓┣━┫┃┗┫┃ ┃┃╺┓┣┳┛┣━┫┣━┛┣━┫┗┳┛                   by
┗━┛ ╹ ┗━╸┗━┛╹ ╹╹ ╹┗━┛┗━┛╹┗╸╹ ╹╹  ╹ ╹ ╹                @mhsattarian

'''
print(MainHeader)

class Steganography:

  def __init__(self, imageColorBits = 8):
    # Assume Images have 8 bit to store colors
    self.imageColorBits = imageColorBits

  # def get_high_order_bits(self, number, numberOfBits = 4):
  #   # Calculate number of bits to shift right
  #   n = self.imageColorBits - numberOfBits
  #   # Shift right to remove extra bits
  #   temp = number >> n
  #   # Return 8-bit Number with just <numberOfBits> hight value bits
  #   return temp << n
  
  # def set_high_order_as_low(self, number, numberOfBits = 4):
  #   # Calculate number of bits to shift right
  #   n = self.imageColorBits - numberOfBits
  #   # Shift right to make high-order bits low-order
  #   return number >> n

  def compress_image(self, image, setLowOrder = False, numberOfBits = 4):
    """Compress image by removing low-order bits"""
    numberOfBits = self.imageColorBits - numberOfBits
    imageShiftedRight = np.right_shift(image, numberOfBits)
    if not setLowOrder: return np.left_shift(imageShiftedRight, numberOfBits)
    else: return imageShiftedRight

  def encode_images(self, image1, image2):
    if type(image1) == 'str': pass
    if type(image1) == 'str': pass
    
    container = self.compress_image(image1)
    containee = self.compress_image(image2, setLowOrder = True)
    
    return container | containee

  def funcname(self, parameter_list):
    pass
    


if __name__ == '__main__':
  container = cv2.imread('images/container.png')
  containee = cv2.imread('images/containee.png')

  s = Steganography()
  output = s.encode_images(container, containee)

  cv2.imwrite("images/output.png", output)
  print("- output stored in Images directory.")

  # cv2.imshow("container", container)
  # cv2.waitKey(0)
  # cv2.imshow("containee", containee)
  # cv2.waitKey(0)
  # cv2.imshow("output", output)
  # cv2.waitKey(0)
  
  # cv2.destroyAllWindows()
