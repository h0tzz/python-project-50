from gendiff.formatters import json, string, plain

available_formatters = {
    'json': json.render,
    'string': string.render,
    'plain': plain.render
}
