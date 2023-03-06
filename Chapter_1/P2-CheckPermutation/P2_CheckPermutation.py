# O(N)

def check_permutation(s1:str, s2:str) -> bool:
    if len(s1) != len(s2):
        return False

    # Assume ASCII char set 128 characters
    s1_char_set = [0 for i in range(128)]
    s2_char_set = [0 for i in range(128)]

    for char in s1:
        s1_char_set[ord(char)] += 1

    for char in s2:
        s2_char_set[ord(char)] += 1


    for c1, c2 in zip(s1_char_set, s2_char_set):
        if c1 != c2:
            return False

    return True
