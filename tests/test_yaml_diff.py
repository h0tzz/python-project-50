# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.generator import generate_diff
import tests.expected as expected


def test1_simple_string():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'string')
    assert actual == expected.SIMPLE_STRING


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'plain')
    assert actual == expected.SIMPLE_PLAIN

