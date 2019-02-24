#!/usr/bin/python3
import cv2
import numpy as np
import click

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
    if type(image1) == str: image1 = cv2.imread(image1)
    if type(image2) == str: image2 = cv2.imread(image2)
    
    container = self.compress_image(image1)
    containee = self.compress_image(image2, setLowOrder = True)
    
    return container | containee

  def decode_image(self, image, numberOfBits = 4):
    if type(image) == str: image = cv2.imread(image)
    
    numberOfBits = self.imageColorBits - numberOfBits
    codedImage = np.bitwise_and(image, pow(2, numberOfBits) - 1)
    return np.left_shift(codedImage, numberOfBits)



if __name__ == '__main__':

  s = Steganography()

  CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
  @click.group(context_settings=CONTEXT_SETTINGS)
  def cli():
      """Hide an image within another"""

  @cli.command('encode', short_help='Encode an image within another')
  @click.argument('container', type=click.Path(exists=True))
  @click.argument('containee', type=click.Path(exists=True))
  @click.option('-o', '--out', help="Specify output file", default="output.png")
  @click.option('--show', help="Display output image", is_flag=True)
  def encode(container, containee, out, show):
    """Encode containee within container"""
    output = s.encode_images(container, containee)
    if show: 
      cv2.imshow("output", output)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    cv2.imwrite(out, output)
    print("- output stored.")

  @cli.command('decode', short_help='Extracts encoded image')
  @click.argument('image', type=click.Path(exists=True))
  @click.option('-o', '--out', help="Specify output file", default="extracted.png")
  @click.option('--show', help="Display output image", is_flag=True)
  def decode(image, out, show):
    """Decode an image and store the extracted image"""
    codedImage = s.decode_image(image)
    if show: 
      cv2.imshow("extracted", codedImage)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    cv2.imwrite(out, codedImage)
    print("- extracted image stored.")


  MainHeader = '''
  ┏━┓╺┳╸┏━╸┏━╸┏━┓┏┓╻┏━┓┏━╸┏━┓┏━┓┏━┓╻ ╻╻ ╻       Hide an Image within another
  ┗━┓ ┃ ┣╸ ┃╺┓┣━┫┃┗┫┃ ┃┃╺┓┣┳┛┣━┫┣━┛┣━┫┗┳┛                   by
  ┗━┛ ╹ ┗━╸┗━┛╹ ╹╹ ╹┗━┛┗━┛╹┗╸╹ ╹╹  ╹ ╹ ╹                @mhsattarian

  '''
  print(MainHeader)

  cli()

  # cv2.imshow("container", container)
  # cv2.waitKey(0)
  # cv2.imshow("containee", containee)
  # cv2.waitKey(0)
  # cv2.imshow("output", output)
  # cv2.waitKey(0)
  
