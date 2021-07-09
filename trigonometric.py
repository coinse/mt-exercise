import pytest
import math
from hypothesis import given
from hypothesis import strategies as st

def sine(radian):
    return taylor(radian, 20)

def taylor(x, n):
    s = 0
    for i in range(n):
        sign = math.pow(-1, i)
        s += sign * x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return s

@given(x=st.floats(min_value=-50.0, max_value=50.0))
def test_sine(x):
    y = math.pi - x
    assert sine(x) == pytest.approx(sine(y), 0.001)

if __name__ == '__main__':
    test_sine()