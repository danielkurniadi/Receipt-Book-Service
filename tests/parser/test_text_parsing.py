import os
import unittest
import yaml

from config import TEST_TEXT_DATA_DIR
from app.parser.text_receipt_parser import (
    parse_sum_in_text,
    parse_market_in_text
)


class TextParserTest(unittest.TestCase):
    """Test for text parsing component
    """
    def test_parse_total_sum(self):
        """Parsing total sum from textual receipt
        """
        sum_test_textfile = os.path.join(TEST_TEXT_DATA_DIR, 'sample_text_receipt_sum.txt')

        # Step 1. prepare sample text file
        with open(sum_test_textfile) as receipt_file:
            receipt_text = receipt_file.read()
        
        receipt_sum = 0.99
        self.assertIsNotNone(receipt_text)

        # Step 1.b prepare additional test case
        additional_testcases = (
            ('Summe  $USD12,99\n', 12.99),
            ('Subtotal  SGD 89.99\n Tax 0.7%\nTotal  SGD 90,19 (discounted)\n', 90.19),
            ('Subtotal  SGD88.88\n Change 11.0\nTotal due SGD98.88\n', 98.88),
            ('Amount due EUR 18.98\n **********', 18.98)
        )

        # Step 2. parse sum in receipt text and verify
        parsed_sum = parse_sum_in_text(receipt_text)
        self.assertEqual(receipt_sum, parsed_sum)

        # Step 2.b parse sum in additional testcase
        for test_text, true_sum in additional_testcases:
            parsed_sum = parse_sum_in_text(test_text)
            self.assertEqual(true_sum, parsed_sum)

    def test_parse_market(self):
        """Parsing market from textual receipt
        """
        market_test_textfile = os.path.join(TEST_TEXT_DATA_DIR, 'sample_text_receipt.txt')

        # Step 1. prepare sample text file
        with open(market_test_textfile) as receipt_file:
            receipt_text = receipt_file.read()
        
        receipt_market = 'CoffeeShop'
        self.assertIsNotNone(receipt_text)

        # # Step 1.b prepare additional test case
        additional_testcases = (
            ('Fair Price NTU  \n ***** Thank you for visiting us ****', 'Grocery'),
            ('Giant NTU\n\n ***** Thank you for visiting us ****', 'Grocery'),
            ('Grocery store  ***** Thank you for visiting us ****', 'Grocery'),
            ('22790\n\n MACS', 'FastFood')
        )

        # Step 2. parse sum in receipt text and verify
        parsed_market = parse_market_in_text(receipt_text)
        self.assertEqual(parsed_market, receipt_market)

        # # # Step 2.b parse sum in additional testcase
        for test_text, correct_market in additional_testcases:
            parsed_market = parse_market_in_text(test_text)
            self.assertEqual(parsed_market, correct_market)
