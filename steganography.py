import cv2
import numpy as np

MainHeader = '''
┏━┓╺┳╸┏━╸┏━╸┏━┓┏┓╻┏━┓┏━╸┏━┓┏━┓┏━┓╻ ╻╻ ╻       Hide an Image within another
┗━┓ ┃ ┣╸ ┃╺┓┣━┫┃┗┫┃ ┃┃╺┓┣┳┛┣━┫┣━┛┣━┫┗┳┛                   by
┗━┛ ╹ ┗━╸┗━┛╹ ╹╹ ╹┗━┛┗━┛╹┗╸╹ ╹╹  ╹ ╹ ╹                @mhsattarian
'''
print(MainHeader)

class steganography:
  def __init__(self):
    # Assume Images have 8 bit to store colors
    self.imageColorBits = 8

  def get_high_order_bits(self, number, numberOfBits = 4):
    # Calculate number of bits to shift right
    n = self.imageColorBits - numberOfBits
    # Shift right to remove extra bits
    temp = number >> n
    # Return 8-bit Number with just <numberOfBits> hight value bits
    return temp << n
  
  def set_high_order_as_low(self, number, numberOfBits = 4):
    # Calculate number of bits to shift right
    n = self.imageColorBits - numberOfBits
    # Shift right to make high-order bits low-order
    return number >> n

  def compress_image(self, image, setLowOrder = False):
    """Compress image by removing low-order bits"""
    h, w = image.shape
    output = np.zeros([h,w], dtype=np.uint8)

    for i in range(h):
      for j in range(w):
        temp = self.get_high_order_bits(image[i, j])
        if setLowOrder: temp = self.set_high_order_as_low(temp)
        output[i, j] = temp
    return output

  def encode_images(self, image1, image2):
    if type(image1) == 'str': pass
    if type(image1) == 'str': pass
    
    container = self.compress_image(image1)
    containee = self.compress_image(image2, setLowOrder = True)
    
    return container | containee
    


if __name__ == '__main__':
  container = cv2.imread('images/container.png', 0)
  containee = cv2.imread('images/containee.png', 0)

  s = steganography()
  output = s.encode_images(container, containee)

  cv2.imshow("container", container)
  cv2.waitKey(0)
  cv2.imshow("containee", containee)
  cv2.waitKey(0)
  cv2.imshow("output", output)
  cv2.waitKey(0)
  
  cv2.destroyAllWindows()
