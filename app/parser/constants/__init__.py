import os
import yaml

from app.parser.libs.object_views import ObjectView


def read_config(config_yaml):
    """
    """
    with open(config_yaml, 'r') as stream:
        try:
            docs = yaml.safe_load(stream)
            return ObjectView(docs)
        except yaml.YAMLError as e:
            raise e