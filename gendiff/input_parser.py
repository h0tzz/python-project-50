"""Input data parser."""

import json

import yaml


def parser(file_data, file_type):
    """Parse input data into appropriate format."""
    mapping = {
        '.json': json.loads,
        '.yml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader),
        '.yaml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader),
    }
    return mapping[file_type](file_data)
