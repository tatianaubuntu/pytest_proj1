import pytest

from utils.dicts import get_val


@pytest.mark.parametrize("collection, key, default, expected", [
    ({"name": "Alisa"}, "name", 'git', "Alisa"),
    ({"user": "Alisa"}, "name", 'git', 'git'),
    ({}, "name", "bazaar", "bazaar")
])
def test_get_val(collection, key, default, expected):
    assert get_val(collection, key, default) == expected
