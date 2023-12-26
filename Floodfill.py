from typing import Tuple, Any, List
import numpy as np
import cv2
from numpy import ndarray
from PIL import Image

# Way 1
img = cv2.imread('stock_img.jpeg', 1)
print(type(img))

'''
print(len(img[0]), len(img))
print(img[0][0])
# 474X474 image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow('image')
'''

# Way 2
'''filename = "stock_img.jpeg"
with Image.open(filename) as img:
    height, width = img.shape
'''


# 1). Task done img imported and converted to workable format


# Search most used color
def most_frequent_color(image) -> tuple[Any, Any]:
    '''We'll use numpy in built library that has np.unique function for which u can refer to the doc attached

    '''
    r_img = img.reshape(-1, img.shape[-1])  # two dimensions pixels and colors
    colors, count = np.unique(r_img, axis=0, return_counts=True)
    max_index = np.argmax(count)
    min_index = np.argmin(count)
    return colors, colors[max_index], colors[min_index]


_, a, b = most_frequent_color(img)
print(a, b)


def color_dump(image, min_color, max_color):
    # Trying bfs
    req_pixels = image[
        (image[:, :, 0] == max_color[0]) & (image[:, :, 1] == max_color[1]) & (image[:, :, 2] == max_color[2])]

    # for i in req_pixels:

    return []


# Replace most used color with a new color
def replace_color(image, old_color, new_color):
    mask = np.all(image == old_color, axis=-1)
    image[mask] = new_color


# Replace most used color with green (you can replace it with the desired color)
replace_color(img, a, b)

# test = color_dump(img, b, a)
cv2.imwrite('stock_img.jpeg', img)
cv2.imshow('stock_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
