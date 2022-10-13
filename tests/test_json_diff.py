from gendiff.generator import generate_diff
import tests.excepted as excepted


def test1_plain_json():
    actual = generate_diff('./tests/fixtures/plain_before.json',
                           './tests/fixtures/plain_after.json', 'json')
    assert actual == excepted.SIMPLE_JSON
