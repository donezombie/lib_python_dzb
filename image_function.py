from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO


def get_width_height(path):
  im = Image.open(path)
  width, height = im.size
  return (width, height)

def get_area(height, start, end):
  top = 0
  left = start
  right = end
  bottom = height
  return (left, top, right, bottom)

def convert_to_base64(img):
  imgByteArr = BytesIO()
  img.save(imgByteArr, format='PNG')
  imgByteArr = imgByteArr.getvalue()
  encode = base64.b64encode(imgByteArr).decode('ascii')
  return 'data:image/jpeg;base64, {}'.format(encode)

def slice_image(path, number_page):
  if (number_page):
    array_img_base64 = []
    # read image
    im = Image.open(path, mode='r')
    # get width/height image
    width, height = get_width_height(path)
    # slice image 
    for i in range(number_page):
      start = width * i / number_page
      end = width * (i + 1) / number_page
      box = get_area(height, start, end)
      img = im.crop(box)
      value_img_base64 = convert_to_base64(img)
      array_img_base64.append(value_img_base64)
    return array_img_base64
  return

if __name__ == "__main__":
  lista = slice_image('../daudo.jpg', 3)
  print(lista)