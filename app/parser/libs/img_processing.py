"""Image processing module for OCR (image to text) parsing.
"""
# !/usr/bin/python3
# coding: utf-8

# Copyright 2019-2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import numpy as np
from PIL import Image


def sharpen_image(np_image):
    """
    Shapening an image

    Args:
        np_image (np.array): Image of numpy matrix
    
    Returns:
        shapened_image (np.array): Sharpened image of numpy matrix
    """
    # unsharp masking: https://en.wikipedia.org/wiki/Unsharp_masking
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    # 2D convolution ops for image sharpening
    sharpened_image = cv2.filter2D(np_image, -1, kernel)
    return sharpened_image


def rotate_image(np_image, angle=-90):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping

    Args:
        np_image (np.array): Image of numpy matrix
        angle (float): angle in degrees
    
    Returns:
        rotated_mat (np.array): Rotated image of numpy matrix
    """

    height, width = np_image.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(np_image, rotation_mat, (bound_w, bound_h))
    return rotated_mat


def deskew_image(np_image):
    """
    Deskew Image by calculating minAreaRect that contains most threshBinary

    Args:
        np_image (np.array): Image of numpy matrix for opencv operation
    
    Returns:
        deskewed_image (np.array): Deskewed image of numpy matrix 
    """
    gray = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)
    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = -angle

    # rotate the image to deskew it
    deskewed_image = rotate_image(np_image, angle)
    return deskewed_image
