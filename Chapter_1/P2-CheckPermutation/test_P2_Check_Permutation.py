from P2_CheckPermutation import check_permutation

def test_check_permutation():
    Ts = [
        ("", ""),
        ("A", "A"),
        ("abcd", "acdb"),
        ("123", "321"),
        ("1122333", "2233113")
    ]

    Fs = [
        ("", "a"),
        ("ac", 'dba'),
        ("123", "3211"),
        ("1", "2")
    ]

    for (s1, s2) in Ts:
        assert check_permutation(s1, s2) is True

    for (s1, s2) in Fs:
        assert check_permutation(s1, s2) is False