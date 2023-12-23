from typing import Tuple, Any

import numpy as np
import cv2
from Collection import List
from numpy import ndarray

# Way 1
img = cv2.imread('stack_img.jpeg', 1)
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
'''img = np.asarray('stack_img.jpeg')'''


# 1). Task done img imported and converted to workable format


# Search most used color
def most_frequent_color(image) -> tuple[Any, Any]:
    '''We'll use numpy in built library that has np.unique function for which u can refer to the doc attached

    '''
    r_img = img.reshape(-1, img.shape[-1])  # two dimensions pixels and colors
    colors, count = np.unique(r_img, axis=0, return_counts=True)
    max_indx = np.argmax(colors)
    min_indx = np.argmin(colors)
    return colors[max_indx], colors[min_indx]


a, b = most_frequent_color(img)
print(a, b)


def color_dump(img, min_color, max_color) -> List[List[int]]:
    # Trying bfs

    return
