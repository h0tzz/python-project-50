# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.generator import generate_diff
import tests.expected as expected


def test1_simple_string():
    actual = generate_diff('./tests/fixtures/simple_before.json',
                           './tests/fixtures/simple_after.json',
                           'string')
    assert actual == expected.SIMPLE_STRING

