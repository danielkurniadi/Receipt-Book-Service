"""Interface for OCR Receipt.
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

import numpy as np
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

from app.parser.libs.img_processing import (
    sharpen_image, deskew_image
)


def ocr_parse_image_to_text(img_stream):
    """Handler image to text
    """
    # image preprocessings
    np_image = np.array(Image.open(img_stream))
    sharpened_image = sharpen_image(np_image)
    deskewed_image = deskew_image(sharpened_image)

    # text detection
    text = pytesseract.image_to_string(Image.fromarray(deskewed_image))

    return text
