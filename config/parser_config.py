"""Configurations setter for parser
"""

import os
import yaml

from config import PARSER_YAML_PATH 

__all__ = ['yaml_config']


class YamlObject(object):
    """Yaml objects as dicts
    """
    def __init__(self, d):
        self.__dict__ = d


def read_config(config=PARSER_YAML_PATH):
    """Helper to read config from yaml file
    """
    with open(config, 'r') as stream:
        try:
            yaml_file = yaml.safe_load(stream)
            return YamlObject(yaml_file)
        except yaml.YAMLError as e:
            raise e


# export yaml_config object
yaml_config = read_config(PARSER_YAML_PATH)
