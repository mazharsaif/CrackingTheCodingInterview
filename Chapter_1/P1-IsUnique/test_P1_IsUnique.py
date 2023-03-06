from P1_IsUnique import is_unique

def test_is_unique():
    assert is_unique("") is True
    assert is_unique("a") is True
    assert is_unique("1234abcd") is True
    assert is_unique("!@#$%^") is True
    assert is_unique("ABA") is False
    assert is_unique("!@#$%^!") is False

if __name__ == "__main__":
    test_is_unique()