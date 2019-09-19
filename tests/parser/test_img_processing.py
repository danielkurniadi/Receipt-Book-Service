"""Module for testing image processing
"""

import os
import unittest
import cv2
import numpy as np
from PIL import Image

from app.parser.libs.img_processing import (
    sharpen_image,
    rotate_image,
    deskew_image
)
from config import (
    TEST_OUTPUT_DIR,
    TEST_IMG_DATA_DIR
)


class ImageProcessingTest(unittest.TestCase):
    """Test for image processing module
    """

    def test_sharpen_image(self):
        """Image sharpening works.
        Matrix validation for sharpened image is out of the scope for now.
        As long as no errors, we can manually see output at tests/test_output/
        """
        np_images = []
        image_filenames = os.listdir(TEST_IMG_DATA_DIR)
        sharpened_outdir = os.path.join(TEST_OUTPUT_DIR, 'sharpen_img')

        os.makedirs(sharpened_outdir, exist_ok=True)

        # Step 1. load all test images to numpy matrix
        for image_filename in image_filenames:
            image_filepath = os.path.join(TEST_IMG_DATA_DIR, image_filename)
            np_images.append(cv2.imread(image_filepath))

        for i, image in enumerate(np_images):
            # Step 2. sharpen images
            sharpened_image = sharpen_image(image)
            
            # Step 3. imwrite to outpath
            sharpened_outpath = os.path.join(sharpened_outdir, 'sharpened_' +image_filenames[i])
            cv2.imwrite(sharpened_outpath, sharpened_image)

    def test_rotate_image(self):
        """Image Rotation works.
        Matrix validation for rotating image is out of the scope for now.
        """
        np_images = []
        image_filenames = os.listdir(TEST_IMG_DATA_DIR)

        # Step 1. load all test images to numpy matrix
        for image_filename in image_filenames:
            image_filepath = os.path.join(TEST_IMG_DATA_DIR, image_filename)
            np_images.append(cv2.imread(image_filepath))

        for i, image in enumerate(np_images):
            # Step 2. rotate images
            rotated_img = rotate_image(image, angle=-90) # 90-degrees clockwise
            
            # Step 3. imwrite to outpath
            rotated_outpath = os.path.join(TEST_OUTPUT_DIR, 'rotate_img', 'rotated_90_' +image_filenames[i])
            cv2.imwrite(rotated_outpath, rotated_img)
