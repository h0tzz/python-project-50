from gendiff.constants import CHANGED, ADDED, REMOVED, UNCHANGED, NESTED


def build_ast(before, after):
    keys = list(before.keys() | after.keys())
    return {key: gen_node(key, before, after) for key in sorted(keys)}


def gen_node(key, before, after):
    before_value = before.get(key)
    after_value = after.get(key)
    node = {}

    if before_value is None:
        node = {
            'type': ADDED,
            'value': _get_value_type(after_value)
        }
    elif isinstance(before_value, dict) and isinstance(after_value, dict):
        node = {
            'type': NESTED,
            'value': build_ast(before_value, after_value),
        }
    elif after_value is None:
        node = {
            'type': REMOVED,
            'value': _get_value_type(before_value)
        }
    elif before_value == after_value:
        node = {
            'type': UNCHANGED,
            'value': _get_value_type(before_value)
        }
    elif before_value != after_value:
        node = {
            'type': CHANGED,
            'old_value': _get_value_type(before_value),
            'new_value': _get_value_type(after_value)
        }

    return node


def _get_value_type(elem_value):
    if elem_value is True:
        return 'true'
    if elem_value is False:
        return 'false'
    return elem_value
