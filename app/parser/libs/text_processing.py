"""Text processing tools
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

import difflib


def clean_normalise_text_lines(input_text_lines):
    """Clear and normalise text
    Includes case lowering and strip (right & left) for whitespace.
    Also replace comma with dots to ease the search of float number

    Args:
        input_text_lines [(str)]: lines of text to be cleaned
    
    Returns:
        cleaned_text_lines [(str)]: text has been cleaned
    """
    cleaned_text_lines = [
        line.lower().strip().replace(',', '.')
        for line in input_text_lines
    ]
    # filter token from empty string element
    return [token for token in cleaned_text_lines if (token != '')]


def fuzzy_find_text_line(input_text_lines, keyword, cutoff=0.6):
    """Fuzzy matching of text lines and keyword. 
    Get line that contains word with the best matching score
    Args:
        input_text_lines [(str)]: lines of text to be fuzzy matched
        keyword (str): keyword for fuzzy matching
        cutoff (float): cutoff score for matching
    
    Returns:
        matched_text (str): a line of first-matched text
    """
    best_score = 0.0
    best_match_line = ""
    for line in input_text_lines:
        # tokenizing words
        words = line.strip().split()
        match = difflib.get_close_matches(keyword, words, 1, cutoff=cutoff)
        if match:
            # when match is found
            # we proceed to update best scoring token
            match = match[0]
            score = difflib.SequenceMatcher(lambda x: x == " ", match, keyword).ratio()
            if score > best_score:
                # update best matching and score
                best_match_line = line
                best_score = score
    return best_match_line
