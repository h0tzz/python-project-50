import os

from gendiff.input_parser import parser
from gendiff.ast_builder import build_ast
from gendiff.formatters import available_formatters


def read_file(file_path):
    with open(file_path, 'r') as file_object:
        file_data = file_object.read()
        file_type = os.path.splitext(file_path)[-1]
        return parser(file_data, file_type)


def generate_diff(first_file_path, second_file_path, output_format='plain'):
    first, second = read_file(first_file_path), read_file(second_file_path)
    ast = build_ast(first, second)
    formatter = available_formatters.get(output_format)
    if not formatter:
        return 'Unsupported formatter'
    return formatter(ast)
