"""Module for text processing
"""

import os
import unittest

from app.parser.libs.text_processing import (
    clean_normalise_text_lines,
    fuzzy_find_text_line
)
from config import TEST_TEXT_DATA_DIR


class TextProcessingTest(unittest.TestCase):
    """Test for text processing module
    """
    def test_fuzzy_matching(self):
        """Fuzzy matching should return a line that contains the
        closest/best matched word in input text with respect to keyword.
        """
        fuzzy_test_textfile = os.path.join(TEST_TEXT_DATA_DIR, 'sample_text_fuzzy_find.txt')
        
        # Step 1. prepare sample text file
        with open(fuzzy_test_textfile) as receipt_file:
            receipt_text_lines = clean_normalise_text_lines(receipt_file.readlines())
        self.assertIsNotNone(receipt_text_lines)

        # Step 2. prepare ground_truth_keyword_pairs for validation
        ground_truth_keyword_pairs = [
            ('Subtotal $15.00', 'subtotal'),
            ('Total $15.00', 'total'),
            ('Tax 95%', 'tax'),
            ('Drive Thru', 'drive'),
            ('Starbucks store', 'store'),
            ('Coffe beans cafe', 'cafe')
        ]

        # Step 3. validate for all ground truth and keyword pairs
        # the fuzzy matching is able to work and come with correct line
        for ground_truth, keyword in ground_truth_keyword_pairs:
            self.assertEqual(
                ground_truth.lower(), 
                fuzzy_find_text_line(receipt_text_lines, keyword, cutoff=0.2)
            )

    def test_clean_normalise_text_lines(self):
        """Cleaning and normalising function should
        strip (left and right) in each line in text, lower case, and replace comma
        with dots
        """
        cleaning_test_textfile = os.path.join(TEST_TEXT_DATA_DIR, 'sample_text_receipt_normalize.txt')
        
        # Step 1. prepare sample text file
        with open(cleaning_test_textfile) as receipt_file:
            receipt_text_lines = clean_normalise_text_lines(receipt_file.readlines())
        self.assertIsNotNone(receipt_text_lines)
        
        # Step 2. prepare ground truth for validation
        ground_truth_tokens = set([
            'all upper case', 'some upper case', 'white spaces',
            'tab     tab whitespaces', '99.00', 
            '$5.80 cent   -0.9 cent  bonus: $90.789',
            'trailing whitespaces after this line.'
        ])
        
        # Step 3. validate cleaned text
        cleaned_text_tokens = set(clean_normalise_text_lines(receipt_text_lines))
        self.assertEqual(ground_truth_tokens, cleaned_text_tokens)
