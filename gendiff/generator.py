import json
from functools import reduce


def generate_diff(first_file_path, second_file_path, output_format):
    first_file, second_file = json.load(
        open(first_file_path)), json.load(open(second_file_path))
    first_file_keys, second_file_keys = first_file.keys(), second_file.keys()

    first_dict = dict(first_file)
    second_dict = dict(second_file)

    deleted_keys = [key for key in first_file_keys if key not in second_file_keys]
    added_keys = [key for key in second_file_keys if key not in first_file_keys]
    updated_keys = [key for key in first_file_keys if key not in deleted_keys + added_keys and first_dict[key] != second_dict[key]]
    unchanged_keys = [key for key in first_file_keys if key in second_file_keys and first_dict[key] == second_dict[key]]

    all_keys = sorted(deleted_keys + added_keys + updated_keys + unchanged_keys)

    def get_key_str(res, key):
        if key in deleted_keys:
            return res + f' - {key}: {first_dict[key]}\n'
        elif key in added_keys:
            return res + f' + {key}: {second_dict[key]}\n'
        elif key in updated_keys:
            return res + f' - {key}: {first_dict[key]}\n + {key}: {dict(second_file)[key]}\n'
        else:
            return res + f'   {key}: {first_dict[key]}\n'

    result = reduce(get_key_str, all_keys, '')

    return f"{{\n{result}}}"


