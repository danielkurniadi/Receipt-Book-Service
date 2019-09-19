"""Interface to text processing for text parsing purposes.
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

import re
from config.parser_config import yaml_config
from app.parser.libs.text_processing import (
    clean_normalise_text_lines,
    fuzzy_find_text_line
)


def parse_market_in_text(text):
    """Parsing text to search for originating market
    """
    text_lines = [line.strip() for line in text.splitlines() if line]
    text_lines = clean_normalise_text_lines(text_lines)

    for cutoff in range(8, 2, -2):
        # gradually decrease the cutoffs from 1.0 to 0.6
        cutoff = float(cutoff/10.0)

        for market_keyword, spellings in yaml_config.market_keywords.items():
            # for each spelling, find fuzzy matching and hence
            # the first match must have the highest matching score
            for spelling in spellings:
                matching_line = fuzzy_find_text_line(text_lines, spelling, cutoff=cutoff)
                if matching_line:
                    return market_keyword
    return ""


def parse_sum_in_text(text):
    """Parsing text to extract decimal total/sum
    
    Args:

    """
    text_lines = [line.strip() for line in text.splitlines() if line]
    text_lines = clean_normalise_text_lines(text_lines)

    for cutoff in range(10, 5, -2):
        # gradually decrease the cutoffs from 1.0 to 0.6
        cutoff = float(cutoff/10.0)
        for sum_keyword in yaml_config.sum_keywords:
            matching_line = fuzzy_find_text_line(text_lines, sum_keyword, cutoff=cutoff)
            if matching_line:
                float_strings = re.findall(yaml_config.sum_pattern, matching_line)
                if float_strings:
                    return float(float_strings[0])
    return -1

