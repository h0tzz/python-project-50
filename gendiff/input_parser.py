import json


def parser(file_data, file_type):
    mapping = {
        '.json': json.loads
    }
    return mapping[file_type](file_data)
