import pytest
import re


def atoi(s: str) -> int:
    if not len(s):
        return 0
    s = re.findall("(^[\+\-0]*\d+)\D*", s.strip())
    print(s)
    try:
        return max(-2 ** 31, min(int(''.join(s)), 2 ** 31 - 1))
    except ValueError:
        return 0


@pytest.mark.parametrize('s, res', [
    ('42', 42),
    ('  -42', -42),
    ('4193 with words', 4193),
    ('words and 987', 0),
    ('-9128347233', -2147483648),
    ('', 0),
])
def test_atoi(s, res):
    assert atoi(s) == res
