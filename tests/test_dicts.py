from utils import dicts


def test_get_val():
    assert dicts.get_val({"name": "Alisa"}, "name") == "Alisa"
    assert dicts.get_val({"user": "Alisa"}, "name", "git") == "git"
    assert dicts.get_val({}, "name", "bazaar") == "bazaar"
